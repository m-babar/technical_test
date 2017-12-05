function Validate() {
        var password = document.getElementById("id_password").value;
        var confirmPassword = document.getElementById("confirm-pass").value;
        var gen_error = document.getElementById("gen_error");

        if (password != confirmPassword) {

            gen_error.innerHTML = 'Password must be same.';
            gen_error.style.color = "red";

            return false;
        }

        return true;
    }


$(document).ready(function(){

  // using jQuery
  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }


  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });









$("#signup_form").on('submit', function(event){
  event.preventDefault();
  var $this_ = $(this);
  let geturl = $this_.attr('data-url');
  var formData = $this_.serialize();

  $.ajax({
    url: geturl,
    type: "POST",
    data:formData,
    success: function (response, status, xhr) {  

    let token = xhr.getResponseHeader('access_token')

      if (response.status == 201) {
        window.location.href = "/dashboard/";
        window.localStorage.setItem('access_token', token );
      }
      else {

          swal({
              title: "Error Occur",
              text: "Please Login again with authorized Email and Password",
              type: "warning",
              showCancelButton: false,
              confirmButtonClass: "btn-danger",
              confirmButtonText: "OK",
              closeOnConfirm: true,
              timer: 5000,
            });    
        window.location.href = "/login/";
        window.localStorage.clear();

      }
    },

    error : function (response) {
         swal({
              title: "Please Enter Correct credientials",
              text: "Your will not be able to Login without authorized Email and Password",
              type: "warning",
              showCancelButton: false,
              confirmButtonClass: "btn-danger",
              confirmButtonText: "OK",
              closeOnConfirm: true,
              timer: 500000,
            });



    }
 
    });





 });
 


 });
 
