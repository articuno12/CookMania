db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
auth = Auth(db)
auth.define_tables()
crud = Crud(db)

password_is_match = IS_MATCH(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}', error_message='password must be atleast 8 characters long,alphanumeric,has atleast one special character and both small and capital letter',
                             search=True)
db.auth_user.password.requires.insert(0, password_is_match)

db.define_table('recipe',
    Field('title','string','length=200'),
    Field('body','text'),
    Field('created_by','reference auth_user',default=auth.user_id),
    Field('created_on','datetime',default=request.now),
    format='%(title)s')

db.define_table('comments',
    Field('recipe_id','reference recipe'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id))

db.define_table('image',
    Field('recipe_id','reference recipe'),
    Field('file','upload'))

db.define_table('hardlike',
    Field('created_by', 'reference auth_user'),
    Field('recipe_id', 'reference recipe'))

db.recipe.title.requires=IS_NOT_IN_DB(db,'recipe.title')
db.recipe.body.requires=IS_NOT_EMPTY()
db.recipe.title.requires=IS_NOT_EMPTY()

db.comments.body.requires=IS_NOT_EMPTY()
db.recipe.created_by.writable=db.recipe.created_by.readable=False
db.comments.created_by.writable=db.comments.created_by.readable=False
db.recipe.created_on.writable=db.recipe.created_on.readable=False
db.comments.created_on.writable=db.comments.created_on.readable=False
db.comments.recipe_id.writable=db.comments.recipe_id.readable=False
db.image.recipe_id.writable=db.image.recipe_id.readable=False

# if auth.is_logged_in() :
#     liked = db(db.likes.created_by == auth.user.id)
#     db.likes.recipe_id.requires=IS_NOT_IN_DB(liked,'likes.recipe_id')
