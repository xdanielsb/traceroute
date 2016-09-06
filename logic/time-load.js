/*
 *Time for loading a page
 */
var page = require("webpage").create();
var system = require("system");
var initDate = Date.now();

url = system.args[1];

page.open(url, function(state){
    timeLoad=Date.now()-initDate;
    console.log("The page has been load in "+timeLoad+  " en mili segundos");
})
