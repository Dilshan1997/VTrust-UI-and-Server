$("#edit_profile").click(()=>{
    $.ajax({
        type:"POST",
        url: 'edit',
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
            if("error_msg" in response){
                $("#custom-message").html(response['error_msg'])
            }
            else{
                window.location.replace("http://127.0.0.1:8000/VTrust/home");
            }
            
            
            // modal.hide()
            
        },
        error: function (response) {
            console.log(response)
            $("#custom-message").html(response)
            $("#custom-message").addClass("alert-error alert-dismissible msg fade show ")
            
        }
    }
    )
})

 


