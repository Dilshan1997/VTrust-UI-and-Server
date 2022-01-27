$( document ).ready(()=>{
  n=$('#ballot_count').text()
  console.log(n)
  for(let i=0;i<n;i++){
$(function () {
    var proposalChart = $("#proposal-analysis-chart"+i);
    console.log(proposalChart);
    $.ajax({
      url: proposalChart.data("url"),
      success: function (data) {
        // console.log(data)
        console.log(data)
        // console.log(proposalChart)
        var ctx = proposalChart[0].getContext("2d");

        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: data.labels,
            datasets: [{
              label: 'Proposals',
              backgroundColor: '#A5FFF9 ',
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
}
})