$("#edit_profile").on("submit",()=>{

    $.ajax({

        type: 'POST',
        url: '{% url "profile_edit" %}',
        data: {
            name:$('#user_edit_name').val(),
            email:$('#user_edit_email').val(),
            old_password:$('#old_password').val(),
            new_password:$('#new_password').val(),
            re_new_password:$('#re_new_password').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'POST'
        },
        success: function (response) {
            console.log(response)
        },
        error: function (response) {
            console.log(response)
        }
    })
})

