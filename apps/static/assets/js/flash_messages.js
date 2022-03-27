// logging key-value pairs of FormData object
function logFormData(data) {
    for (const pair of data.entries()) {
        console.log(pair[0] + ": " + pair[1]);
    }
}


// fade out message alerts
function fade_alerts() {
    alerts = document.getElementsByClassName("alert_msg_js");
        var i = alerts.length;
        for (let elem of alerts) {
            i--;
            time = 3250+(1000*i);
            setTimeout(function() {
                $(elem).fadeOut("slow");
            }, time);
        }
}

// call fade out after DOMContentLoaded
window.addEventListener('DOMContentLoaded', (event) => {
    fade_alerts();
});