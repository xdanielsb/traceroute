var page = require("webpage").create();
var times  = 0;
var url = "https://gambadilegno.noc.seabone.net/lg/lg.cgi";
var ip = "216.58.192.68"; 

page.onLoadFinished = function (){
    console.log("the page load for "+times +" times");
    if(times == 1){
      console.log(page.content);
    }
    times = times +1;
};

page.open(url,function(status){
        page.evaluate(function(){
            /*
            //Select the option for tracing the route
            trace = document.getElementsByTagName('input')[5];
            trace.checked = true;
            //Select the input
            input = document.getElementsByTagName('input')[6];
            //Change the address
            input.value = ip;
            //Submit the form
            submit = document.getElementsByTagName("input")[7];
            submit.click();
            */
        });
        console.log(page.content);
})



