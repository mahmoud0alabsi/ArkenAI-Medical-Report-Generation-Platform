function getCookie(name) {
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


const dropArea = document.querySelector(".drop_box"),
  dragText = dropArea.querySelector("header");

const button = document.getElementById("upload_file_btn");
const input = document.getElementById("uploaded_file");

let file;
var filename;

button.onclick = () => {
  input.click();
};

input.addEventListener("change", function (e) {
  var fileName = e.target.files[0].name;

  document.getElementById("uploaded_file_name").innerHTML = fileName;
  file = e.target.files[0];
});





// Give event listener to the submit button
$("#submit").on("click", function (event) {
  event.preventDefault();
  let btn = $(this);

  // document.getElementById("alert").innerHTML = "Recorde Submited";

  //   change the button text and disable it
  btn.html("Submitting...").prop("disabled", true).addClass("disable-btn");
  //   create a new File with the recordedData and its name
  const recordedFile = new File([player.recordedData], `audiorecord.webm`);
  //   grabs the value of the title field
  // const title = document.getElementById("title").value;
  //   initializes an empty FormData
  let data = new FormData();
  //   appends the recorded file and title value
  data.append("recorded_audio", recordedFile);
  // data.append("title", title);
  data.append("submit_recorded_audio", "");

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

        document.getElementById("alert").style.display = "none";

        btn.html("Submit").prop("enabled", true);

        document.getElementById("outputTextarea").value = response.response;

        // activate save modal btn
        $("#save_report_btn").prop("disabled", false);


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

0// Give event listener to the submit button
$("#submit_uploaded").on("click", function (event) {
  event.preventDefault();

  if (file != null) {
    let btn = $(this);
    //   change the button text and disable it
    btn.html("Submitting...").prop("disabled", true);
    //   create a new File with the recordedData and its name
    const uploadedFile = file;// uploaded_file.files[0];
    //   initializes an empty FormData
    let data = new FormData();
    //   appends the recorded file and title value
    data.append("recorded_audio", uploadedFile);
    data.append("submit_uploaded_audio", "");

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

          document.getElementById("alert").style.display = "none";

          btn.html("Submit").prop("disabled", false);

          document.getElementById("outputTextarea").value = response.response;

          // activate save modal btn
          $("#save_report_btn").prop("disabled", false);

          file = null;
          document.getElementById("uploaded_file_name").innerHTML = "";

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
  }
  else {
    document.getElementById("uploaded_file_name").innerHTML = "Please select a file";
  }


});





// Save record when click this btn
$("#save_report_btn").on("click", function (event) {

  event.preventDefault();
  let btn = $(this);
  //   change the button text and disable it
  btn.html("Saving...").prop("disabled", true);
  document.getElementById("save_spinner").style.display = "block";
  //   grabs the value of the title field
  const OutputText = document.getElementById("outputTextarea").value;
  const Title = document.getElementById("reportTitle").value;
  //   initializes an empty FormData
  let data = new FormData();
  //   appends the recorded file and title value
  data.append("outputTextarea", OutputText);
  data.append("reportTitle", Title);
  // data.append("title", title);
  data.append("submit_save_response", "");

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
        document.getElementById("save_spinner").style.display = "none";
        document.getElementById("saving_done_alert").style.display = "block";

        btn.html("Save").prop("disabled", true);

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
$("#close_modal_btn").on("click", function (event) {
  event.preventDefault();

  document.getElementById("saving_done_alert").style.display = "none";
  document.getElementById("reportTitle").value = '';
  // document.getElementById("save_report_btn").prop("disabled", false);

});


// activate upload file submit button when upload new file
var up = document.getElementById("uploaded_file");
up.onchange = function () {
  // activate save modal btn
  $("#submit_uploaded").prop("disabled", false);
};
