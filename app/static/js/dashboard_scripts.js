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

      console.log(copyText.value);
    }




    const csrftoken = getCookie2('csrftoken'); //$("[name=csrfmiddlewaretoken]").val();
    if (csrftoken) {
      function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
      }
      $.ajaxSetup({
        beforeSend: function (xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        },
      });
    }