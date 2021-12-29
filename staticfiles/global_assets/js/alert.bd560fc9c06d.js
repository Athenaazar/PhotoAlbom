$(document).ready(function () {
    console.log("ready!");
    let errorMessage = $('#error-message').val()
    console.log(errorMessage)
    if ((errorMessage !== null) && (errorMessage !== undefined) && (errorMessage !== "")) {
        new PNotify({
            title: 'خطا',
            text: errorMessage,
            icon: 'icon-blocked',
            type: 'error'
        });
    }
});