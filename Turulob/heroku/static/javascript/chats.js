


$('.messageinput').keyup(function () {
  // If value is not empty
  if ($(this).val().length == 0) {
    // Hide the element
    $('#messageimage').show();
  } else {
    // Otherwise show it
    $('#messageimage').hide();
  }
}).keyup();



function myredirect(myurl1) {
  location.href = myurl1;
}

function myredirectimage(myurl2){
  location.href=myurl2;
}

function myredirectstickers(myurl3){
  location.href=myurl3;
}

$(window).bind('onpopstate', function(){
  location.href = "/chats";
});











// ajax request formate 
// ajax request formate 
// ajax request formate 
{/* function sendMessage() {
            const chat = document.getElementById("messageinput").value;
            const url1 = `/chats/{{touser}}/send`
            $.ajax({
                data: {
                    chats: chat
                },
                url: url1,
                type: 'POST',
                success: function (response) {
                    console.log("success")
                },
                error: function (response) {
                    console.log("error")

                }
            });
            console.log(chat)
        }; */}