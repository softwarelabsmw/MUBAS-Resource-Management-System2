
// Bookings per resource
  $(function () {

    var $dailybookingChart = $("#daily-booking-chart");
    $.ajax({
      url: $dailybookingChart.data("url"),
      success: function (data) {

        var ctx = $dailybookingChart[0].getContext("2d");

        new Chart(ctx, {
          type: 'line',
          data: {
            labels: data.labels,
            datasets: [{
              label: "Bookings",
              backgroundColor: ['#3e95cd', '#8e5ea2'],
              data: data.data
            }]
          },
          options: {
            responsive: true,
            legend:  { display: true },
            title: {
              display: true,
              text: 'Number of Resources'
            }
          }
        });

      }
    });

  })