function showPopUp(id){
    console.log(id)
    $.ajax({
        type: 'GET',
        url: "ballot/winner/"+id,
        
        success: function (response) {
            console.log(response)
            $('#winner_details_'+id).html('<h3 class="px-lg-5 font-medium">Name</h3><span><h3 >'+response['proposal_data'][1]+'</h3></span><h3 class="px-lg-5 font-medium">Vote Count</h3><span><h3>'+response['proposal_data'][3] +'</h3></span>')
        },
        error: function (response) {
            console.log(response)
        }
    })


}





