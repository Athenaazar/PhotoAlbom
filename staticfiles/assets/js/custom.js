function showAlert(message_text, type) {
    alerts.push({'text': message_text, 'type': type});
    pNotify.init();
    setInterval(function () {
        alerts = [];
    }, 1000);
}

function deleteCategory(e) {
    let category_uuid = e.value;
    let csrf = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: '/delete-category/',
        type: 'POST',
        data: {
            "category_uuid": category_uuid,
            csrfmiddlewaretoken: csrf
        },

        success: function (data) {
            if (data.status === "ok") {
                // showAlert(data.message_text, "error")
                window.location = data.url;
            } else if (data.status === "error") {
                let message_text = data.message_text
                showAlert(message_text, "error")
            }
        },
        error: function () {
            let message_text = "some error occurred!"
            showAlert(message_text, "error")
        },
    })
}

function picturesListSelectCategory(e) {
    e.preventDefault();
    let category_selection_element = document.getElementById("category_selection")
    if (category_selection_element.value === "") {
        (function () {
            $(category_selection_element).next("span").html("choose a category.")
        })();
    } else {
        (function () {
            $(category_selection_element).next("span").html("")
        })();
        $('#getSelectedCategoryPicturesForm').submit();
    }
}