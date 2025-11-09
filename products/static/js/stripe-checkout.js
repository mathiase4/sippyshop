/** 
* Stripe checkout javascript
* handles stripe payment card Element and form submission
*/


// Stripe Card Element style configuration 
var stripeCardStyle = {
    base: {
        color: '#000',
        fontSize: '16px',
        '::placeholder': {
            color: '#d4c9bb'
        }
    },
    invalid: {
        color: '#dc3545'
    }
};

// stripe and elements
var stripe = Stripe(stripePublicKey); // stripe public key from checkout.html
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
var displayError = document.getElementById('card-errors');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    // Disable submit button to prevent double submission
    submitButton.disabled = true;
    buttonText.classList.add('d-none');
    spinner.classList.remove('d-none');
    displayError.textContent = '';


    var billingDetails = {
        name: form.full_name.value,
        email: form.email.value,
        phone: form.phone.value,
        address: {
            line1: form.address_line1.value,
            line2: form.address_line2.value,
            city: form.city.value,
            country: form.country.value,
            postal_code: form.postal_code.value
        }
    };

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: cardElement,
            billing_details: billingDetails
        }
    }).then(function(results) {
        if (results.error) {
            displayError.textContent = results.error.message;

            submitButton.disabled = false;
            buttonText.classList.remove('d-none');
            spinner.classList.add('d-none');

        } else {
            if (results.paymentIntent.status === 'succeeded') {

                var hiddenInput = document.getElementById('payment_intent');

                hiddenInput.value = results.paymentIntent.id;

                form.submit();
            }
        }
    });

});