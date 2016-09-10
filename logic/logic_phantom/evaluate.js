var page = require("webpage").create();
var system = require("system");
/*
 * Fetch me the title of the page 
 */
url = system.args[1];
namepage = system.args[2];
console.log(url);

page.open(url,function(status){

    var title  = page.evaluate(function(){
        return document.title;
    })
    console.log(title);
    phantom.exit();
})

