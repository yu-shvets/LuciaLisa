$(document).ready(function(){
  $(".slide-one").owlCarousel();

  $(".slide-two").owlCarousel();

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


$('.slide-one').owlCarousel({
    animateOut: 'slideOutDown',
    animateIn: 'flipInX',
    items:1,
    smartSpeed:450,
    loop:true,
    autoplay:true,
    autoplayTimeout:100
});

$(".slide-two").owlCarousel({
    items:3,
});
