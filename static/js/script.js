window.addEventListener('scroll', function() {

    var header = this.document.querySelector('.fixed-nav');
    header.classList.toggle('sticky', window.scrollY > 35);
    if (this.scrollY > 35) {
        header.style.boxShadow = "-13px 13px 24px -11px rgba(0,0,0,0.1)";
    } else {
        header.style.boxShadow = "None";

    }


})
let index = 0
setInterval(function() {
    const images = ['test.jpg.crdownload', 'test2.jpg', 'slide-04.jpg', 'slide-01.jpg']
    var mains = document.querySelector('main.home_main');

    mains.style.backgroundImage = `url(/static/images/${images[index]})`;
    index = (index + 1) % images.length

}, 5000)

document.addEventListener('DOMContentLoaded', function() {
    $('main .text a').css({ 'transform': 'scale(1)' })
    $('main .text h3 ').addClass('style');
    $('main .text p ').addClass('style');
});




window.addEventListener('scroll', function() {
    const scroll_poisition = 260;
    if (this.scrollY >= scroll_poisition) {
        myfunc();
    }

    function myfunc() {
        var shop_now = document.querySelectorAll('.shop_now');
        shop_now.forEach(function(item) {

            item.style.animationName = 'animi';
            item.style.animationDuration = '0.9s';
            item.style.animationTimingFunction = 'ease-in-out';
        })

    }

})






// ______________
$('.right .shopping-cart').click(function() {
    $('aside').css({ 'right': '0px' })

})
$('aside .close').click(function() {
        $('aside').css({ 'right': '-350px' })
    })
    // _____________


window.addEventListener('scroll', function() {
    if (this.scrollY > 500) {
        $('.scroll_to_top').css({ 'display': 'block' })
    } else {

        $('.scroll_to_top').css({ 'display': 'none' })
    }


})
$('.scroll_to_top').click(function() {

    window.scrollTo({
            top: 0,
            behavior: "smooth"
        }

    )

})