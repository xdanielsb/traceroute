/*
 *This code take an screenshot of a page that I have already specify
 *
 */

/*
 *For scrapping the page
 */
var page = require("webpage").create();
var system = require("system");
/*
 * Take and screenshot of the page
 */
url = system.args[1];
namepage = system.args[2];
console.log(url);
console.log(namepage);
page.open(url,function(status){
    page.render(namepage+".png");
    phantom.exit();
})

