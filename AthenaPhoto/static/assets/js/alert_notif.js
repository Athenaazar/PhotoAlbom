let pNotify = function () {
    //
    // Setup module components
    //

    let stack_custom_bottom = {"dir1": "right", "dir2": "up", "spacing1": 1};
    let stack_bottom_left_rtl = {"dir1": "left", "dir2": "up", "push": "top"};

    let _componentPnotify = function () {
        if (typeof PNotify === 'undefined') {
            console.warn('Warning - pnotify.min.js is not loaded.');
            return;
        }

        //
        // Notification styles
        //

        // Bottom right
        function show_stack_bottom_right(text, type) {
            let opts = {
                text: text,
                type: 'primary',
                addclass: "stack-bottom-right bg-primary-400 border-primary",
                stack: $('html').attr('dir') === 'rtl' ? stack_bottom_left_rtl : stack_custom_bottom
            };

            switch (type) {
                case 'error':
                    opts.addclass = "stack-bottom-right bg-danger-400 border-danger";
                    opts.type = type;
                    break;

                case 'info':
                    opts.addclass = "stack-bottom-right bg-info-400 border-info";
                    opts.type = type;
                    break;

                case 'success':
                    opts.addclass = "stack-bottom-right bg-success-400 border-success";
                    opts.type = type;
                    break;

                case 'warning':
                    opts.addclass = "stack-bottom-right bg-warning-400 border-warning";
                    opts.type = type;
                    break;
            }
            new PNotify(opts);
        }

        $(document).ready(function () {
            let i;
            for (i = 0; i < alerts.length; i++) {
                // let alert = alerts.pop();
                // show_stack_bottom_right(alert['text'], alert['type']);
                show_stack_bottom_right(alerts[i]['text'], alerts[i]['type']);
            }
        });
    };

    //
    // Return objects assigned to module
    //

    return {
        init: function () {
            _componentPnotify();
        }
    }
}();


// Initialize module
// ------------------------------

document.addEventListener('DOMContentLoaded', function () {
    pNotify.init();
});


function showAlert(text, alertType) {
    alerts.push({'text': text, 'type': alertType});
    pNotify.init();
}
