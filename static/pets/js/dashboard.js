var date_valid = false

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('-');
}

    function isFutureDate(idate){
        var today = new Date();
        var todaydate = formatDate(today);
        // idate = idate.split("-");

        idate = new Date(idate);
        return (today - idate) < 0 ? true : false;
    }

    function check_Date() {
        // var idate = document.getElementById("birthday").value;
        var idate = $( ".birthday" ).val();

            if(isFutureDate(idate)) {
                $( "div.datewarn" ).html('Please enter valid date.') 
                $( "div.datewarn" ).css('color', 'red')
                return false
            } 

            else {
                $( "div.datewarn" ).html('✓')  
                $( "div.datewarn" ).css('color', 'green') 
                  return true;
            }
    }

function validateForm() {
    date_valid = check_Date()

    if( date_valid == true){
        return true;
    }
    else { 
        resultDIV = document.getElementById("all_form_invalid").innerHTML = "Please fill valid field."
        return false;
      }
    }


$(document).ready(function(){

    let get_data = function() {
      let $details_container = $("#details");
      let $pet_details_ul  = $('#pet_details_ul');

      let items = [];

        let token = localStorage.access_token

                $.ajax({
                  url: "/user/pets/",
                  type: "GET",
                  headers: { 'Authorization': "Token " + localStorage.access_token },
                  data: { },
                  success: function(data,) {  
                        $('.signup-btn').css('display' , 'none');      
                        $('.signin-btn').css('display' , 'none');      
                        $('.logout-btn').css('display' , 'inline');      

                    if (data.length == 0)  {
                        $('#nodata').css('display' , 'inline-block');
                        $('#showdata').css('display' , 'none');      

                    }
                    else {
                        $('#nodata').css('display' , 'none');
                        $('#showdata').css('display' , 'inline-block');      

                        $.each(data, function( index, value ) {

                            let pet_type = value.pet_type;
                            if( pet_type == 'C' || pet_type=='c') {     pet_type = 'Cat'    }
                            else {  pet_type = 'Dog'    }
                            let pet_name = value.name;
                            let birthday = value.birthday;
                            let pet_id = value.id;

                           $("#details").append( 
                          "<ul id="+ pet_id + "><li>" + pet_type + "</li> <li>" + pet_name  + "</li> <li>" + birthday + 
                          "</li> <li>  <button  type=button class='pet-update btn btn-primary' id='pet_update' pet_id=" + pet_id + " > Update </button> </li>" +
                          " <li> <button type=button class='pet-delete btn btn-danger' id='pet_delete' pet_id=" + pet_id + " > Delete </button> </li></ul><br>"
                          );
                        });
                      }
                    },
                  error: function(errors, status) { 
                    if(status == 401) {
                        window.alert("you are not Authorized person.")
                        window.location.href = "/";
                        window.localStorage.clear()
                        
                    }
                    else {    
                        window.location.href = "/";
                        window.localStorage.clear()
                    }
                  }
                });
    }

get_data();


$(document).on("submit", "#pet_form", function(event){

    event.preventDefault();
    var $this_ = $(this);
    var formData = $this_.serialize();

    let $details_container = $("#details");
    let $pet_details_ul  = $('#pet_details_ul');
    let items = []; 
    let output = [];

    $.ajax({
        url: "/user/pets/",
        type: "POST",
        headers: { 'Authorization': "Token " + localStorage.access_token },
        data: formData,

        success: function (data, status, xhr) {  
            $('.close_modal').click()

            if (status == 'success') {
                $('#showdata').css('display' , 'inline-block');      

                let pet_type = data.pet_type;
                let pet_name = data.name;
                let birthday = data.birthday;
                let pet_id = data.id;

                $("#details").append( 
                "<ul id=" + pet_id + " ><li>" + pet_type + "</li> <li>" + pet_name  + "</li> <li>" + birthday + 
                "</li> <li>  <button  type=button class='pet-update btn btn-primary' id='pet_update' pet_id=" + pet_id + " data-pet_id=" + pet_id + " > Update </button> </li>" +
                " <li> <button type=button class='pet-delete btn btn-danger' id='pet_delete' pet_id=" + pet_id + " data-pet_id=" + pet_id + " > Delete </button> </li></ul><br>"
                );

                swal({
                  title: "Successfully Created",
                  text: "Pet Successfully created.",
                  type: "success", 
                  allowOutsideClick: false,
                  timer:2000,})


                }
              },

              error: function (response, xhr, error) {
                alert(error);    
                alert(response.status);    
              }
      });
});


$(document.body).on("click", ".pet-update", function(event){

          event.preventDefault();
          var $this_ = $(this);
          let pet_id = $this_.attr('pet_id');

          $.ajax({
          url: "/user/pets/" + pet_id + "/",
          type: "GET",
          headers: { 'Authorization': "Token " + localStorage.access_token },
          data: { },
          success: function (response, status, xhr) {  

                    if (status == 'success') {
                      console.log()
                      $('#UpdateModal').modal('show');

                      $(".modal-body").val($('select[name="pet_type"]').val( response[0].pet_type ));
                      $(".modal-body").val($('input[name="name"]').val( response[0].name ));
                      $(".modal-body").val($('input[name="birthday"]').val( response[0].birthday ));

                      $(".modal-body").attr('pet_id', response[0].id)

                    }
                    else {
                      alert("Invalid credientials ");    
                    }
                  },

          error: function (response, xhr, error) {
            alert(error)    
            alert(response.error)    
          }
          });

});



$(document.body).on("submit", "#update_form", function(event){

    let pet_id =  $(".modal-body").attr('pet_id')

    event.preventDefault();
    var $this_ = $(this);
    var formData = $this_.serialize();

    $.ajax({
      url: "/user/pets/" + pet_id + "/",
      type: "PUT",
      headers: { 'Authorization': "Token " + localStorage.access_token },
      data: formData,
      success: function (data, status, xhr) {  

        if (status == 'success') {

            $('.close_modal').click()
          
            let pet_type = data.pet_type;
            let pet_name = data.name;
            let birthday = data.birthday;
            let pet_id = data.id;

            $("#"+ pet_id +"").remove();

            $("#details").append( 
            "<ul id=" + pet_id + " ><li>" + pet_type + "</li> <li>" + pet_name  + "</li> <li>" + birthday + 
            "</li> <li>  <button  type=button class='pet-update btn btn-primary' id='pet_update' pet_id=" + pet_id + "  > Update </button> </li>" +
            " <li> <button type=button class='pet-delete btn btn-danger' id='pet_delete' pet_id=" + pet_id + "  > Delete </button> </li></ul><br>"
            );

            swal({
                title: "Successfully Update",
                text: "Pet details Successfully Update.",
                type: "success", 
                allowOutsideClick: false,
                timer:3000,  })
           
        }
        else {  
            swal({
                title: "Error",
                text: "Something went wrong.",
                type: "warning", 
                allowOutsideClick: false,
                timer:2000,})

          alert("Invalid credientials ");    
        }
      },
      error: function (response, xhr, error) {
                  console.log(response);
                  console.log(xhr);
                  console.log(error);
      }
    });
});


$(document.body).on("click", ".pet-delete", function(event){
  
    let pet_id = $(this).attr('pet_id')

    $.ajax({
        url: "/user/pets/" + pet_id + "/",
        type: "delete",
        headers: { 'Authorization': "Token " + localStorage.access_token },
        data: { },
        success: function (response, status, xhr) {  

        if (status == 'success') {

            swal({
                title: "Successfully Deleted",
                text: "Pet Detail Successfully Deleted.",
                type: "success", 
                allowOutsideClick: false,
                timer:2000,  })



          $("#details").empty();
          get_data();
        }

        else {
          alert("Invalid credientials ");    
        }
      },

      error: function (response, xhr, error) {
        alert(error)    
        alert(response.error)    
      }
    });
 });







// logout
$('.logout-btn').on('click', function() { 

  $.ajax({
    url: "/user/logout/",
    type: "POST",
    headers: { 'Authorization': "Token " + localStorage.access_token },
    data: { "token": localStorage.access_token },
    success: function (response, status, xhr) {  
        console.log(response)
        if (response.status == 200) {
            alert(response.message)

            window.localStorage.clear()
            window.location.href = "/";


      }

      else {
        alert("Invalid credientials ");    
      }
    },

    error: function (response, status) {

      window.localStorage.clear()
      window.location.href = "/";


    }
  });
 });
 });


