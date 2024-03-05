function setAlarm() {
    const minutes = document.getElementById('minutes').value;
    const seconds = document.getElementById('seconds').value;
    fetch(`/set_alarm?minutes=${minutes}&seconds=${seconds}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to set alarm');
            }
            console.log('Alarm set successfully');
        })
        .catch(error => {
            console.error(error.message);
        });
}

function startAlarm() {
    fetch('/start_alarm')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to start alarm');
            }
            console.log('Alarm started');
        })
        .catch(error => {
            console.error(error.message);
        });
}
