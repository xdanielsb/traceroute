var page = require("webpage").create();
page.open("http://www.google.com", function(status){
    console.log("the page was loaded" +status);
})
