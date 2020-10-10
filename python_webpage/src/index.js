

$( document ).ready(function() {
    
    let func_fetch_status = function fetch_status()
    {

        $.get("/getStatus", function(current_status){
            console.log(current_status)

            if (current_status.state == 0){
                document.getElementById("overlay_shoe").style.left = "0%"
            } else if (current_status.state == 1){
                document.getElementById("overlay_shoe").style.left = "33.33%"
            } else if (current_status.state == 2){
                document.getElementById("overlay_shoe").style.left = "66.66%"
            }

            if (current_status.shoes == true) {
                document.getElementById("overlay_shoe").style.opacity = "100%"
            } else {
                document.getElementById("overlay_shoe").style.opacity = "30%"
            }

            document.getElementById("middlepane").innerHTML = "Temp:" + String(current_status.temperature) + "\nHumidity:" + String(current_status.humidity)
            
            if (current_status.status === "heating") {
                document.getElementById("middlepane").style.backgroundColor == "#f86300a8"
            } else {
                document.getElementById("middlepane").style.backgroundColor == "#fa8537a8"
            }
            
            // document.getElementById("div_status").innerHTML = result.pos

        });
    }


    setInterval(func_fetch_status,1000)


});

// setInterval(function(){ alert("time"); }, 3000);

// alert("hello")


function move(){
    console.log("asdasd")
    let cur_x = document.getElementById("overlay_shoe").style.left
    cur_x = cur_x.substr(0,cur_x.length-1)
    cur_x = Number(cur_x)
    cur_x +=1
    // console.log(document.getElementById("overlay_shoe").style.left)
    document.getElementById("overlay_shoe").style.left = String(cur_x)+ "%"
    // this.style.left +=10;
}


