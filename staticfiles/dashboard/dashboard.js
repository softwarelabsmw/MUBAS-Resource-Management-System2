// Set up
  const labels = [
    'CIT',
    'Commerce',
    'Engineering',
    'Media Studies',
    'Technical Team',
    'Management',
  ];

  const data = {
    labels: labels,
    datasets: [{
      label: 'DAILY BOOKING TREND',
      backgroundColor: 'rgb(18, 5, 166)',
      borderColor: 'rgb(18, 5, 166)',
      data: [0, 10, 5, 2, 20, 30, 45],
    }]
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };

// Config
  const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );


// Total Students per Class Pie Chart By Gender
  $(function () {

    var $dailybookingChart = $("#daily-booking-chart");
    $.ajax({
      url: $dailybookingChart.data("url"),
      success: function (data) {

        var ctx = $dailybookingChart[0].getContext("2d");

        new Chart(ctx, {
          type: 'pie',
          data: {
            labels: data.labels,
            datasets: [{
              label: "Number of Products",
              backgroundColor: ['#3e95cd', '#8e5ea2'],
              data: data.data
            }]
          },
          options: {
            responsive: true,
            legend:  { display: true },
            title: {
              display: true,
              text: 'Number of Products'
            }
          }
        });

      }
    });

  })