
function getCookie(name) {
    var dc = document.cookie;
    var prefix = name + "=";
    var begin = dc.indexOf("; " + prefix);
    if (begin == -1) {
        begin = dc.indexOf(prefix);
        if (begin != 0) return null;
    }
    else {
        begin += 2;
        var end = document.cookie.indexOf(";", begin);
        if (end == -1) {
            end = dc.length;
        }
    }
    // because unescape has been deprecated, replaced with decodeURI
    //return unescape(dc.substring(begin + prefix.length, end));
    return decodeURI(dc.substring(begin + prefix.length, end));
}

function getCookie2(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


//--------------- Display Report ---------------
// Get a reference to all the buttons with class "myButton"
var buttons = document.querySelectorAll(".myButton");

// Add a click event listener to each button
buttons.forEach(function (button) {
    button.addEventListener("click", function () {

        // Get the button's name attribute
        var id = button.getAttribute("name");

        let data = new FormData();
        //   appends the recorded file and title value
        data.append("id", id);
        // data.append("title", title);
        data.append("display_report_btn", "");

        const csrftoken = getCookie2('csrftoken');

        //   post url endpoint
        const url = "";
        $.ajax({
            url: url,
            method: "POST",
            data: data,
            dataType: "json",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": csrftoken, // getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
            },
            success: function (response) {
                if (response.success) {

                    document.getElementById("outputTextarea").value = response.response.saved_response;
                    document.getElementById("audio_source_1").src = response.response.voice_record
                    document.getElementById("audio_source_2").src = response.response.voice_record
                    document.getElementById("audio_place").load();


                } else {
                    btn.html("Error").prop("disabled", false);
                }
            },
            error: function (error) {
                console.error(error);
            },
            cache: false,
            processData: false,
            contentType: false,
        });

    });
});


//--------------- Edit Report ---------------
// Get a reference to all the buttons with class "myButton"
var editBtn = document.querySelectorAll(".editReportBtn");

// Add a click event listener to each button
editBtn.forEach(function (button) {
    button.addEventListener("click", function () {

        // Get the button's name attribute
        var id = button.getAttribute("name");

        let data = new FormData();
        //   appends the recorded file and title value
        data.append("id", id);
        // data.append("title", title);
        data.append("display_report_btn", "");

        //   post url endpoint
        const url = "";
        $.ajax({
            url: url,
            method: "POST",
            data: data,
            dataType: "json",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
            },
            success: function (response) {
                if (response.success) {


                    document.getElementById("modalReportTitle").value = response.response.title;
                    document.getElementById("modalTextarea").value = response.response.saved_response;

                    document.getElementById("save_edit_report_btn").setAttribute('id_of_select_obj', response.response.id);
                    //   // activate save modal btn
                    //   $("#save_report_btn").prop("disabled", false);


                } else {
                    btn.html("Error").prop("disabled", false);
                }
            },
            error: function (error) {
                console.error(error);
            },
            cache: false,
            processData: false,
            contentType: false,
        });

    });
});



let saveDon_toRefresh = false;

//--------------- Save Edit Report ---------------
// Get a reference to all the buttons with class "myButton"
var saveEditBtn = document.getElementById("save_edit_report_btn");

// Add a click event listener to each button
saveEditBtn.addEventListener("click", function (event) {
    event.preventDefault();

    var id = document.getElementById("save_edit_report_btn").getAttribute('id_of_select_obj');

    // Get the Title and report text
    let newTitle = document.getElementById("modalReportTitle").value;
    let newReport = document.getElementById("modalTextarea").value;

    console.log(id);
    console.log(newTitle);
    console.log(newReport);

    let data = new FormData();

    data.append("id", id);
    data.append("newTitle", newTitle);
    data.append("newReport", newReport);

    data.append("save_edit_report_btn", "");

    //   post url endpoint
    const url = "";
    $.ajax({
        url: url,
        method: "POST",
        data: data,
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
        },
        success: function (response) {
            if (response.success) {

                document.getElementById("edit_done_alert").style.display = "block";

                $("#save_edit_report_btn").prop("disabled", true);

                saveDon_toRefresh = true;


            } else {
                btn.html("Error").prop("disabled", false);
            }
        },
        error: function (error) {
            console.error(error);
        },
        cache: false,
        processData: false,
        contentType: false,
    });

});



// Save button controler
var txtArea = document.getElementById("modalTextarea");
txtArea.onchange = function () {
    // activate save modal btn
    $("#save_edit_report_btn").prop("disabled", false);
};

var title = document.getElementById("modalReportTitle");
title.onchange = function () {
    // activate save modal btn
    $("#save_edit_report_btn").prop("disabled", false);
};



// hide alert from modal when click (Close) btn
$("#close_modal_btn").on("click", function (event) {
    event.preventDefault();

    if (saveDon_toRefresh) {
        document.getElementById("edit_done_alert").style.display = "none";
        $("#save_edit_report_btn").prop("disabled", true);

        // Refresh the page
        location.reload();
    }
    else {
        document.getElementById("edit_done_alert").style.display = "none";
        $("#save_edit_report_btn").prop("disabled", true);
    }


});








//--------------- Delete Report ---------------
// Get a reference to all the buttons with class "myButton"
var deleteBtn = document.querySelectorAll(".deleteReportBtn");

// Add a click event listener to each button
deleteBtn.forEach(function (button) {
    button.addEventListener("click", function () {

        // Get the button's name attribute
        var id = button.getAttribute("name");

        let data = new FormData();
        //   appends the recorded file and title value
        data.append("id", id);
        // data.append("title", title);
        data.append("display_report_btn", "");

        //   post url endpoint
        const url = "";
        $.ajax({
            url: url,
            method: "POST",
            data: data,
            dataType: "json",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
            },
            success: function (response) {
                if (response.success) {

                    document.getElementById("delete_report_btn").setAttribute('id_of_select_obj', response.response.id);
                    $("#titleOfReportSpan").html(response.response.title);
                    $("#delete_report_btn").prop("disabled", false);

                } else {
                    btn.html("Error").prop("disabled", false);
                }
            },
            error: function (error) {
                console.error(error);
            },
            cache: false,
            processData: false,
            contentType: false,
        });

    });
});

let deleteDon_toRefresh = false;
//--------------- Save Delete Report ---------------
// Get a reference to all the buttons with class "myButton"
var saveEditBtn = document.getElementById("delete_report_btn");

// Add a click event listener to each button
saveEditBtn.addEventListener("click", function (event) {
    event.preventDefault();

    var id = document.getElementById("delete_report_btn").getAttribute('id_of_select_obj');

    let data = new FormData();

    data.append("id", id);

    data.append("delete_report_btn", "");

    //   post url endpoint
    const url = "";
    $.ajax({
        url: url,
        method: "POST",
        data: data,
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
        },
        success: function (response) {
            if (response.success) {

                document.getElementById("delete_done_alert").style.display = "block";

                $("#delete_report_btn").prop("disabled", true);

                deleteDon_toRefresh = true;


            } else {
                btn.html("Error").prop("disabled", false);
            }
        },
        error: function (error) {
            console.error(error);
        },
        cache: false,
        processData: false,
        contentType: false,
    });

});





// hide alert from modal when click (Close) btn
$("#close_delete_modal_btn").on("click", function (event) {
    event.preventDefault();

    if (deleteDon_toRefresh) {
        document.getElementById("delete_done_alert").style.display = "none";
        // Refresh the page
        location.reload();
    }
    else {
        document.getElementById("delete_done_alert").style.display = "none";
    }


});





//--------------- Report Text Area controls ---------------
const textarea = document.getElementById('outputTextarea');
const increaseButton = document.getElementById('increase-font');
const decreaseButton = document.getElementById('decrease-font');

increaseButton.addEventListener('click', function () {
    const currentSize = parseInt(window.getComputedStyle(textarea).fontSize);
    const newSize = currentSize + 2; // Increase font size by 2 pixels
    textarea.style.fontSize = newSize + 'px';
});

decreaseButton.addEventListener('click', function () {
    const currentSize = parseInt(window.getComputedStyle(textarea).fontSize);
    const newSize = Math.max(currentSize - 2, 12); // Decrease font size by 2 pixels, with a minimum of 12px
    textarea.style.fontSize = newSize + 'px';
});


function copyText() {
    let copyText =
        document.getElementById("outputTextarea");

    copyText.select();

    document.execCommand("copy");
}