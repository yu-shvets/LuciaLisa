$(document).ready(function(){
  $(".owl-carousel").owlCarousel();
});
$('.owl-carousel').owlCarousel({
    animateOut: 'slideOutDown',
    animateIn: 'flipInX',
    items:1,
    smartSpeed:450,
    loop:true,
    autoplay:true,
    autoplayTimeout:100
});
