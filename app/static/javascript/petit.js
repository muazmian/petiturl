var host = "http://localhost:5000";

$(document).ready(function(){
    $("#makeItPetit").click(function() {
        var val = $("#url").val();
        val = $.trim(val)
        if(val == "")
            return

        var url = {
            url : val
        }

        $.ajax ({
            url: "/petiturl",
            method: "POST",
            data: url,
            dataType: "json"
        }).success(function(data) {
            var link = host+"/"+data.petiturl
            var a = "<a href='"+link+"'>"+link+"</a>"
            $("#url-output").html(a);
        });
    })
})
