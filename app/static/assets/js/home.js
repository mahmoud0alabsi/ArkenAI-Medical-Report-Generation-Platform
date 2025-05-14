
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



//--------------- Send Book Demo ---------------
// Get a reference to all the buttons with class "myButton"
var sendBookDemo = document.getElementById("submit_send_book_btn");

// Add a click event listener to each button
sendBookDemo.addEventListener("click", function (event) {
    event.preventDefault();

    document.querySelector('.loading').classList.add('d-block');

    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var institution = document.getElementById("institution").value;
    var phone = document.getElementById("phone").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;

    console.log(name);
    console.log(email);
    console.log(message);

    let data = new FormData();

    data.append("name", name);
    data.append("email", email);
    data.append("institution", institution);
    data.append("phone", phone);
    data.append("subject", subject);
    data.append("message", message);

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
            "X-CSRFToken": csrftoken, //getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
        },
        success: function (response) {
            if (response.success) {

                document.querySelector('.loading').classList.remove('d-block');
                document.querySelector('.sent-message').classList.add('d-block');

                // document.getElementById("edit_done_alert").style.display = "block";

                // $("#save_edit_report_btn").prop("disabled", true);

                // saveDon_toRefresh = true;

                console.log("************ All done **********")


            } else {
                document.querySelector('.loading').classList.remove('d-block');
                document.querySelector('.error-message').innerHTML = "Error when try send email, ";
                document.querySelector('.error-message').classList.add('d-block');
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






// // Save button controler
// var txtArea = document.getElementById("modalTextarea");
// txtArea.onchange = function () {
//     // activate save modal btn
//     $("#save_edit_report_btn").prop("disabled", false);
// };

// var title = document.getElementById("modalReportTitle");
// title.onchange = function () {
//     // activate save modal btn
//     $("#save_edit_report_btn").prop("disabled", false);
// };



// // hide alert from modal when click (Close) btn
// $("#close_modal_btn").on("click", function (event) {
//     event.preventDefault();

//     if (saveDon_toRefresh) {
//         document.getElementById("edit_done_alert").style.display = "none";
//         $("#save_edit_report_btn").prop("disabled", true);

//         // Refresh the page
//         location.reload();
//     }
//     else {
//         document.getElementById("edit_done_alert").style.display = "none";
//         $("#save_edit_report_btn").prop("disabled", true);
//     }


// });





