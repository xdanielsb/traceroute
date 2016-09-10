var page = require("webpage").create();
var times  = 0;
page.onLoadFinished = function (){
    console.log("the page load for "+times +" times");
    if(times == 1){
        var val = page.evaluate(function(){
            routers = document.getElementsByName("router");   
            query = document.getElementsByName("query");
            query = document.getElementsByName("sourceIP");
            ipaddress = document.getElementsByName("addr")[0];
            return ipaddress;
           // ipaddress.value =  "216.58.222.238";
        });  
        console.log(page.content);
     //   page.render("pagefont.png");
    }
    times = times +1;
};


page.open("https://www.us.ntt.net/support/looking-glass/",function(status){
    page.evaluate(function(){  
        accept = document.getElementById("toc"); 
        if (accept.type == "checkbox") {
            accept.checked = true;
            console.log("checked");
        }
        inputs = document.getElementsByTagName("input");
        var submit;
        for (var i = 0; i < inputs.length; i++) {
            if(inputs[i].value == "Submit"){
               submit = inputs[i]; 
               submit.click();
            }
        }

    })

})

