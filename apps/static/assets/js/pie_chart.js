$( document ).ready(()=>{
  n=$('#ballot_count').text()
  for(let i=0;i<n;i++){
$(function () {
    var proposalChart = $("#proposal-analysis-chart"+i);
    $.ajax({
      url: proposalChart.data("url"),
      success: function (data) {
        // console.log(data)
        // console.log(proposalChart)
        var ctx = proposalChart[0].getContext("2d");
        new Chart(ctx, {
          type: 'horizontalBar', //'doughnut'
          data: {
            labels: data.labels,
            datasets: [{
              label: 'Proposals',
              backgroundColor:  ['rgba(56, 1, 235, 0.2)',
                                'rgba(54, 162, 235, 0.2)',
                                'rgba(153, 102, 255, 0.2)'],
              data: data.data
            }]          
          },
          options: {
            responsive: true,
            legend: {
              position: 'top',
            },
            scales: {
              xAxes: [{
      
                ticks: {
                  min: 0
                }
              }],
              yAxes: [{
        
              }],
            },
            title: {
              display: true,
              text: 'Proposal Analysis Chart'
            },
     
          }
        });

      }
    });

  });
}
})