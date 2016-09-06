var page = require("webpage").create();
var system = require("system");
/*
 * Change the style of the page
 */
url = system.args[1];
namepage = system.args[2];
console.log(url);

page.open(url,function(status){
    //evaluate the page
    
    page.evaluate(function(){
        document.body.style.background = "blue"
    })
    
    //take the screenshot
    page.render(namepage+".png");
    //close the connection to phantoml
    phantom.exit();
})

