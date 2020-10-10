

$( document ).ready(function() {
    
    // let func_fetch_status = function fetch_status()
    // {

    //     $.get("/getStatus", function(result){
    //         console.log(result)
    //         document.getElementById("div_status").innerHTML = result.pos

    //     });
    // }


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


