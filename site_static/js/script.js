$(function () {
    var slide = $(".slide");
    var slideSize = slide.size();
    var slideNav = $(".slider-nav").find('li');
    var speed = 1000; //время появления слайда
    var time = 6000; // промежуток времени,через которое меняются слайды
    slide.not(":first").hide();
    for (var i = 0; i < slideSize - 1; i++) {
        slideNav.eq(0).clone(true).appendTo(".slider-nav");
    }
    slideNav.eq(0).addClass("active");
    function rotate() {
        var slideNav = $(".slider-nav").find('li');
        var k = $(".slide.active").index();
        if (k < slideSize - 1) {
            slideNav.eq(k).removeClass("active").next().addClass("active");
            slide.eq(k).fadeOut(speed).removeClass("active").next().dequeue().fadeIn(speed).addClass("active");
        }
        else {
            slide.eq(k).fadeOut(speed).removeClass("active");
            slideNav.eq(k).removeClass("active");
            slide.eq(0).dequeue().fadeIn(speed).addClass("active");
            slideNav.eq(0).addClass("active");
        }

    }

    var autoplay = setInterval(rotate, time);

    $(document).on('click', '.slider-nav li', function () {
        var slideNav = $(".slider-nav").find('li');
        if (!$(this).hasClass("active")) {
            if (!slide.is(":animated")) {
                clearInterval(autoplay);
                var ind = $(this).index();
                slide.removeClass('active').fadeOut();
                slideNav.removeClass('active');
                slide.eq(ind).addClass('active').dequeue().fadeIn();
                slideNav.eq(ind).addClass('active');
                autoplay = setInterval(rotate, time);
            }
        }
    });

    var title = $(".block__title");
    title.click(function(){
        var switchBlock = $(this).parent().find(".block__hidden");
        if(switchBlock.is(":visible")){
            switchBlock.slideUp();
            $(this).removeClass("active");
        }
        else{
            switchBlock.slideDown();
            $(this).addClass("active");
        }
    })
});