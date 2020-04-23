function slow_scroll(id){
    $('html, body').animate({
        scrollTop: $(id).offset().top + 20
    }, 500);
    return false;
}
function to_top(){
    $(window).on('scroll', () => {
        if ($(this).scrollTop() >= 250){
            $('.arrow_to_top').fadeIn();
        }
        else {
            $('.arrow_to_top').fadeOut();
        }
    })
}

to_top();