function update_time_choices() {
    var dateField = document.getElementById("id_reservation_date");
    var timeField = document.getElementById("id_reservation_time");
    var selectedDate = dateField.value;

    // Convert the selected date to a JavaScript Date object
    var jsDate = new Date(selectedDate);
    var currentDate = new Date(); // Current date

    // Get the difference in milliseconds between selected date and current date
    var timeDifference = jsDate.getTime() - currentDate.getTime();

    // Calculate the difference in days
    var differenceInDays = Math.floor(timeDifference / (1000 * 3600 * 24));

    // If the selected date is in the past or more than 14 days in the future, remove all times
    if (jsDate < currentDate || differenceInDays > 14) {
        timeField.options.length = 0; // Clear existing options
        return; // Exit the function
    }

    // Get the day of the week (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
    var dayOfWeek = jsDate.getDay();

    // Define operating hours based on the day of the week
    var operatingHours = {
        0: null,  // Sunday
        1: ['11:00', '22:00'],  // Monday
        2: ['11:00', '22:00'],  // Tuesday
        3: ['11:00', '22:00'],  // Wednesday
        4: ['11:00', '22:00'],  // Thursday
        5: ['10:00', '23:00'],  // Friday
        6: ['09:00', '23:00'],  // Saturday
    };

    // Get the operating hours for the selected day
    var hoursForDay = operatingHours[dayOfWeek];

    // Calculate closing time minus 2 hours
    var closingTimeMinus2Hours;
    if (hoursForDay) {
        closingTimeMinus2Hours = new Date(jsDate);
        closingTimeMinus2Hours.setHours(parseInt(hoursForDay[1].split(":")[0]) - 2);
    }

    // Generate time choices within operating hours, up to 2 hours prior to closing
    var interval = 15;
    var choices = [];
    if (hoursForDay) {
        for (var hour = parseInt(hoursForDay[0].split(":")[0]); hour <= closingTimeMinus2Hours.getHours(); hour++) {
            for (var minute = 0; minute < 60; minute += interval) {
                var formattedHour = hour.toString().padStart(2, '0');
                var formattedMinute = minute.toString().padStart(2, '0');
                var timeString = formattedHour + ':' + formattedMinute;
                choices.push([timeString, timeString]);
            }
        }
    }

    // Update the choices in the time field
    timeField.options.length = 0;  // Clear existing options
    for (var i = 0; i < choices.length; i++) {
        var option = new Option(choices[i][0], choices[i][1]);
        timeField.options.add(option);
    }
}
