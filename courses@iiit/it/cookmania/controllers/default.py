def user():
    return dict(form=auth())

@auth.requires_membership('manager')
def manage():
    grid = SQLFORM.smartgrid(db.recipe,linked_tables=['comments','image','hardlike'])
    return dict(grid=grid)

def index():
    if len(request.args): page=int(request.args[0])
    else: page=0
    items_per_page=10
    limitby=(page*items_per_page,(page+1)*items_per_page+1)
    #rows=db().select(db.recipe.ALL,limitby=limitby)
    pages=db().select(db.recipe.id,db.recipe.title,db.recipe.created_by,orderby=~db.recipe.id,limitby=limitby)
    return dict(page=page,items_per_page=items_per_page,pages=pages)

@auth.requires_login()
def create():
    form = SQLFORM(db.recipe)
    if form.process().accepted:
        session.flash="Add image "
        redirect(URL('addimages',args=form.vars.id))
    return dict(form=form)

def show():
    this_page = db.recipe(request.args(0,cast=int)) or redirect(URL('index'))
    db.comments.recipe_id.default=this_page.id
    db.image.recipe_id.defaut=this_page.id
    form=SQLFORM(db.comments).process() if auth.user else "login"
    pagecomments = db(db.comments.recipe_id==this_page.id).select()
    images= db(db.image.recipe_id==this_page.id).select()
    like = db(db.hardlike.recipe_id == this_page.id).select()
    no_likes = len(like)
    return dict(page=this_page, comments=pagecomments, form=form,images=images,li=no_likes)


def download():
    return response.download(request, db)

@auth.requires_login()
def addimages():
    r=db.recipe(request.args(0,cast=int))
    db.image.recipe_id.default=r.id
    form=SQLFORM(db.image)
    form.add_button('Done',URL('show',args=r.id))
    if form.process().accepted:
        session.flash="Image Added"
    if form.errors:
        session.flash="TRY Again"
    images=db(db.image.recipe_id==r.id).select()
    return dict(form=form,images=images)

@auth.requires_login()
def edit():
    this_page=db.recipe(request.args(0,cast=int)) or redirect(URL('index'))
    if not this_page.created_by==auth.user_id :
        session.flash="You cant edit this"
        redirect(URL('show',args=request.args))
    form=SQLFORM(db.recipe,this_page).process(next=URL('show',args=request.args))
    return dict(form=form)

@auth.requires_login()
def mypages():
    if len(request.args): page=int(request.args[0])
    else: page=0
    items_per_page=10
    limitby=(page*items_per_page,(page+1)*items_per_page+1)
    r=db(db.recipe.created_by==auth.user_id).select(db.recipe.ALL,orderby=~db.recipe.id,limitby=limitby)
    #rows=db().select(db.recipe.ALL,limitby=limitby)
    return dict(page=page,items_per_page=items_per_page,recipes=r)


@auth.requires_login()
def add_like() :
    this_page = db.recipe[request.vars.idunique]
    ret = db((db.hardlike.created_by==auth.user_id) & (db.hardlike.recipe_id==this_page.id) ).select()
    if len(ret)>0 :
        # already_liked=(db.hardlike.created_by == auth.user_id) & (db.hardlike.recipe_id == this_page.id )
        db(db.hardlike.id==ret[0].id).delete()
        session.flash = "Unliked"
    else :
        db.hardlike.insert(created_by=auth.user_id,recipe_id=this_page.id)
    nohardlike = len(db(db.hardlike.recipe_id == this_page.id).select())
    # return str(this_page.id)
    return str(nohardlike)
