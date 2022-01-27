$( document ).ready(()=>{
$(function () {
    var proposalChart = $("#proposal-analysis-chart");
    console.log(proposalChart);
    $.ajax({
      url: proposalChart.data("url"),
      success: function (data) {
        // console.log(data)
        console.log(data)
        console.log(proposalChart)
        var ctx = proposalChart[0].getContext("2d");

        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: data.labels,
            datasets: [{
              label: 'Proposals',
              backgroundColor: '#A59F69 ',
              data: data.data
            }]          
          },
          options: {
            responsive: true,
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Proposal Analysis Chart'
            }
          }
        });

      }
    });

  });
})