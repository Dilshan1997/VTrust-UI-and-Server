document.addEventListener('DOMContentLoaded', function (e) {
    FormValidation.formValidation(document.getElementById('loginForm'), {
        fields: {
            username: {
                validators: {
                    notEmpty: {
                        message: 'The username is required',
                    },
                    stringLength: {
                        min: 6,
                        max: 30,
                        message: 'The username must be more than 6 and less than 30 characters long',
                    },
                    regexp: {
                        regexp: /^[a-zA-Z0-9_]+$/,
                        message: 'The username can only consist of alphabetical, number and underscore',
                    },
                },
            },
            password: {
                validators: {
                    notEmpty: {
                        message: 'The password is required',
                    },
                    stringLength: {
                        min: 8,
                        message: 'The password must have at least 8 characters',
                    },
                },
            },
        },
    });
});