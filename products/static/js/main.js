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
var hamburger = document.getElementById('hamburger');
var navMenu = document.getElementById('navMenu');

if (hamburger && navMenu) {
    hamburger.addEventListener('click', function () {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // close menu when clicking on a link //
    var navLinks = document.querySelectorAll('.nav-links a');
    navLinks.forEach(function (link) {
        link.addEventListener('click', function () {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

}
//============
// Product detail quantity (+ or -)
//============
var qtyInput = document.getElementById('quantity');
var qtyHidden = document.getElementById('quantity-hidden');
var qtyIncrease = document.getElementById('increase');
var qtyDecrease = document.getElementById('decrease');

// only use if them all exists 
if (qtyInput && qtyHidden && qtyIncrease && qtyDecrease) {
    qtyIncrease.addEventListener('click', function () {
        var current = Number(qtyInput.value);
        current = current + 1;
        qtyInput.value = current;
        qtyHidden.value = current;
    });

    qtyDecrease.addEventListener('click', function () {
        var current = Number(qtyInput.value);
    if (current > 1) {
        current = current - 1;
        qtyInput.value = current;
        qtyHidden.value = current;
    }
    });

    qtyInput.addEventListener('input', function () {
        var current = Number(qtyInput.value);
        if (current < 1 || isNaN(current)) {
            current = 1;
        }
        qtyInput.value = current;
        qtyHidden.value = current;
});

}

