// Toast Messages //
setTimeout(function () {
    var toasts = document.querySelectorAll('.toast-custom');
toasts.forEach(function (toast) {
    toast.classList.add('hide');
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
        scrollBtn.classList.remove('show');
    }
};

// scroll to top when clicked //
scrollBtn.onclick = function () {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
};

// Mobile Hamburger Menu //
const hamburger = document.getElementById('hamburger');
const navMenu = document.getElementById('navMenu');

if (hamburger && navMenu) {
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // close menu when clicking on a link //
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

}
//============
// Product detail quantity (+ or -)
//============
const qtyInput = document.getElementById('quantity');
const qtyHidden = document.getElementById('quantity-hidden');
const qtyIncrease = document.getElementById('increase')
const qtyDecrease = document.getElementById('decrease');

// only use if them all exists 
if (qtyInput && qtyHidden && qtyIncrease && qtyDecrease) {
    qtyIncrease.addEventListener('click', function () {
        let current = Number(qtyInput.value);
        current = current + 1;
        qtyInput.value = current;
        qtyHidden.value = current;
    });

    qtyDecrease.addEventListener('click', function () {
        let current = Number(qtyInput.value);
    if (current > 1) {
        current = current - 1;
        qtyInput.value = current;
        qtyHidden.value = current;
    }
    });

    qtyInput.addEventListener('input', function () {
        let current = Number(qtyInput.value);
        if (current < 1 || isNaN(current)) {
            current = 1;
        }
        qtyInput.value = current;
        qtyHidden.value = current;
});

}