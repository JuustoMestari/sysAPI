$(function()
{
  $("#btnTest").click(function()
  {
        var APIURI = $("#apiURI").val()+"test";

        var secretKey=$("#secretKey").val();
        var accessKey=$("#accessKey").val();

        var thetime = Date.now();
        var message = "GET "+APIURI+"\n"+String(thetime);
        var signature = CryptoJS.HmacSHA1(message+secretKey,accessKey);

        signature=signature.toString(CryptoJS.enc.Base64);

        $("#testResult").empty();
        $.ajax({
           url: APIURI,
           type: 'GET',
           headers: {
            "X-Date": thetime,
            "Authorization":accessKey+':'+signature
           },
           error: function(response)
           {
                $("#testResult").html("<pre>"+response.responseText+"</pre>");
           },
           success: function(data)
           {
                $("#testResult").html("<pre>"+data+"</pre>");
           }
        });
  });
});