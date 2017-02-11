 me_ajax: function(u, s, t) {
    /*simple ajax function*/
    query = '';
    if(typeof s == "string") {
      d = $(s).serialize();
      if(d) {
        query = d;
      }
    } else {
      pcs = [];
      if(s != null && s != undefined)
        for(i = 0; i < s.length; i++) {
          q = $("[name=" + s[i] + "]").serialize();
          if(q) {
            pcs.push(q);
          }
        }
      if(pcs.length > 0) {
        query = pcs.join("&");
      }
    }
    $.ajax({
      type: "POST",
      url: u,
      data: query,
      success: function(msg) {

        $('#'+t).val(msg);


      }
    });
  };
