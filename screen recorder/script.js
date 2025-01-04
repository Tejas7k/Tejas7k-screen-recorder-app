const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');
const statusDiv = document.getElementById('status');

// Start Recording
startBtn.addEventListener('click', () => {
    startBtn.disabled = true;
    stopBtn.disabled = false;
    statusDiv.textContent = "Status: Recording...";
    
    // Make a POST request to start the Python recording script
    fetch('/start-recording', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
    })
    .catch(error => console.error('Error:', error));
});

// Stop Recording
stopBtn.addEventListener('click', () => {
    startBtn.disabled = false;
    stopBtn.disabled = true;
    statusDiv.textContent = "Status: Stopped";

    // Make a POST request to stop the Python recording script
    fetch('/stop-recording', {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        alert('Recording saved as output.mp4');
    })
    .catch(error => console.error('Error:', error));
});
