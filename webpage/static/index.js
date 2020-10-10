alert("hello")

$( document ).ready(function() {
    console.log( "ready!" );
});

let func_fetch_status = function fetch_status()
{
    // $.get("/getStatus", function(result){
    //     console.log(result)
    //     document.getElementById("div_status").innerHTML = result.pos

    // });
}

document.getElementById("overlay_shoe").style.display = "block";


setInterval(func_fetch_status,1000)

function move(){
    console.log("asdasd")
    this.style.left +=10;
}

