function privateInvitation(b_id){
    console.log(b_id)
    var wallet_address=$('#inviter_wallet_address_'+b_id).val();
    console.log(wallet_address)
    $.ajax({
        type: 'GET',
        url: "invite/"+b_id+"/"+wallet_address,
        
        success: function (response) {
            console.log(response)
            $('#modal_'+b_id).modal('toggle');
            $("#send_or_not").addClass('new-class',"fa-solid fa-envelope fa-bounce" );
        },
        error: function (response) {
            console.log(response)
            $("#send_or_not").text('Error');
        }
    })
  }
  // $("#invitation_btn").click(()=>{
  //   var wallet_address=$('#inviter_wallet_address').val()
  // })
