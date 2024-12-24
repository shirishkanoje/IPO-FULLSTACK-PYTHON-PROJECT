// Fetch IPO statistics from the backend
fetch('http://127.0.0.1:8000/api/ipo-statistics/')
  .then(response => response.json())
  .then(data => {
    document.getElementById('total-ipo').textContent = data.total_ipo;
    document.getElementById('ipo-gain').textContent = data.ipo_in_gain;
    document.getElementById('ipo-loss').textContent = data.ipo_in_loss;

    // Update chart
    const ctx = document.getElementById('ipoChart').getContext('2d');
    new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: ['Upcoming', 'New Listed', 'Ongoing'],
        datasets: [{
          data: [15, 25, 2],
          backgroundColor: ['#36a2eb', '#ff6384', '#ffce56'],
        }]
      },
    });
  });
