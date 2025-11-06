// Toast Messages //
setTimeout(function () {
    var toasts = document.querySelectorAll('.toast-custom');
toasts.forEach(function (toast) {
    toast.classlist.add('hide');
    setTimeout(function () {
        toast.style.display = 'none';
    }, 500);
});
}, 4000);

// scroll to top button //
var scrollBtn = document.getElementById('scrollTopBtn');

// show button when scrolled down 300px //
window.onscroll = function () {
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        scrollBtn.classList.add('show');
    } else {
        scrollBtn.classList.add('show');
    }
};

// scroll to top when clicked //
scrollBtn.onclick = function () {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
};