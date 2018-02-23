$('document').ready(function(){


  //var update_size = $('.update_size');
  //
  //  update_size.on('select', function(e){
  //
  //      var form = $(this).parent('form');
  //
  //      $.ajax({
  //          url : form.attr('action'),
  //          type : "POST",
  //          data : form.serialize(),
  //
  //          success: function(json){
  //              $('#price').text(json.price);
  //          },
  //          error: function(e){
  //              console.log(e);
  //          }
  //      });
  //
  //  });
    $('#id_size').change(function(e){
        //var item = $(this);
        //console.log(item.val());
        var form = $(this).parent('form');
        $.ajax({
            url : form.attr('action'),
            type : "POST",
            data : form.serialize(),

            success: function(json){
                console.log(json);
                $('#price').text(json.price);
                $('#size_id').val(json.size_id);
            },
            error: function(e){
                console.log(e);
            }
        });
    });


    $('#mail_form').on('submit', function(e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
        url: form.attr('action'),
        method: 'post',
        data: form.serialize(),

        success: function (json) {
            console.log('Hello!');
            $('#message').text(json.message);
            form.each(function(){
            this.reset();
            });
        }
    });
});

    $('#feedback_form').on('submit', function(e) {
    e.preventDefault();
    var feedback = $(this);
    $.ajax({
        url: feedback.attr('action'),
        method: 'post',
        data: feedback.serialize(),

        success: function (json) {
            console.log('Hello!');
            $('#feedback').prepend(json.feedback + "<br>" + json.name + " " + json.created);
            feedback.each(function(){
            this.reset();
            });
        }
    });
});


});