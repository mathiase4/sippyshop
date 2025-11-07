/** 
* Stripe checkout javascript
* handles stripe payment card Element and form submission
*/


// Stripe Card Element style configuration 
const stripeCardStyle = {
    base: {
        color: '#fff',
        fontSize: '16px',
        '::placeholder': {
            color: '#d4c9bb'
        }
    },
    invalid: {
        color: '#dc3545'
    }
};

// Stripe with public key 
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Create Stripe card elements 
var cardElement = elements.create('card', {
    style: stripeCardStyle
});

cardElement.mount('#card-element');

// handle real-time validation errors from the card element
cardElement.on('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});

// handle form submission
var form = document.getElementById('payment-form');
var submitButton = document.getElementById('submit-button');
var buttonText = document.getElementById('button-text');
var spinner = document.getElementById('spinner');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    // Disable submit button to prevent double submission
    submitButton.disabled = true;
    buttonText.classList.add('d-none');
    spinner.classList.remove('d-none');

    
    form.submit();
});