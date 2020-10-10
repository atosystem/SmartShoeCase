

$( document ).ready(function() {
    
    let func_fetch_status = function fetch_status()
    {

        $.get("/getStatus", function(result){
            console.log(result)
            document.getElementById("div_status").innerHTML = result.pos

        });
    }


    setInterval(func_fetch_status,1000)


});

// setInterval(function(){ alert("time"); }, 3000);

alert("hello")

