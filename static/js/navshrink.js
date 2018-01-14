$(document).ready(function () {
    var scroll_start = 0
    var startchange = $('#banner-back');
    var offset = startchange.offset();
     if (startchange.length){
         $(document).scroll(function(){
             scroll_start = $(this).scrollTop();
             if(scroll_start > offset.top){
                 $('.navbar-default').css('background-color', '#8c8c8c')
                 $('.navbar-nav li a').css('opacity', '0.6')
             } else{
                $('.navbar-default').css('background-color', 'transparent')
             }
         });

     }
});

$('a[href^="#"]').on('click', function(event) {
    var target = $(this.getAttribute('href'));
    var navHeight = parseInt($('#menuBar').css('height'));
    if( target.length ) {
        event.preventDefault();
        $('html, body').stop().animate({
            scrollTop: target.offset().top-navHeight
        }, 700);}});