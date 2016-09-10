var page = require("webpage").create();
var times  = 0;
var url = "http://ipstats.globalcrossing.net/cgi-bin/lg/lg.cgi?lgCall=r2htrace";
var ip = "216.58.192.68";



page.open(url,function(status){
   

    page.evaluate(function(ip){
        //Select the source router
        document.getElementsByTagName('option')[7].selected = 'selected';
        //Select the input
        input = document.getElementsByName("destAddress")[0] ;
        //Change the address
        input.value = ip;
        //Submit the form
        submit = document.getElementsByTagName("input")[3];
        submit.click();

        
    }, ip);
})



