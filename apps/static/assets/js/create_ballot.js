var proposal_input = $('#prop_num');
var f_next_button = $('#fn_btn');
var x

console.log(proposal_input)
f_next_button.click(() => {
    x = proposal_input.val();
    console.log(x);
    $.ajax({
        type: 'GET',
        url: "create/proposal_num",
        data: { "prop_count": x },
        success: function (response) {

        },
        error: function (response) {
            console.log(response)
        }
    })

    var container = $('<div />');
    for (var i = 1; i <= x; i++) {
        container.append('<h3 class="h3">Proposal' + i + '</h3><div class="col-lg-4 col-sm-6"><div class="mb-4"><label>Proposal Name</label><input type="text" class="form-control"  id=\"prop_name_' + i + '\" name=\"prop_name_' + i + '\"/></div></div></div> <div class="col-lg-4 col-sm-6"><div class="mb-4"><label >Proposal Details</label><input type="text" class="form-control name=\"prop_details_' + i + '\" id=\"prop_details_' + i + '\"" /></div></div></div>');
    }
    $('#cont').html(container);
    //  console.log($('#propname_1'))

})
// var prop_name=$('#propname_1');
// console.log(prop_name)

//Data structure which pass into server via ajax
var proposals_details_arr = [];
var proposals_obj = {};

$("#sn_btn").on('click', () => {
    console.log(x)
    for (var i = 1; i <= x; i++) {
        var proposal_data = {}
        if ($('#prop_name_' + i).val() == "" || $('#prop_details_' + i).val() == !"") {
            proposals_obj["error"] = "Plz fill the all fields"
        }
        else {
            delete proposals_obj["error"]
            proposal_data['pid'] = i - 1
            proposal_data['prop_name'] = ($('#prop_name_' + i).val())
            proposal_data['prop_details'] = ($('#prop_details_' + i).val())
            // proposals_obj['prop'+i]=($('#prop_name_'+i).val());
            // proposal_details['prop'+i]['prop_details']=($('#prop_details_'+i).val());

            proposals_obj["prop" + i] = proposal_data;

        }
    }


    $.ajax({

        type: 'POST',
        url: "create/proposal_data",
        data: { "prop_data": JSON.stringify(proposals_obj) },
        success: function (response) {

        },
        error: function (response) {
            console.log(response)
        }
    })

})
