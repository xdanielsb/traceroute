
var url = 'http://ipstats.globalcrossing.net/cgi-bin/lg/lg.cgi?lgCall=r2htrace';
var ip = "216.58.192.68"
//var url2 = 'http://phantomjs.org';

var casper = require('casper').create({
    pageSettings: {
        loadImages:  false,        // The WebPage instance used by Casper will
        loadPlugins: false         // use these settings
    },
    logLevel: "debug",              // Only "info" level messages will be logged
    verbose: true                  // log messages will be printed out to the console
});


// print out all the messages in the headless browser context
casper.on('remote.message', function(msg) {
    this.echo('remote message caught: ' + msg);
});

// print out all the messages in the headless browser context
casper.on("page.error", function(msg, trace) {
    this.echo("Page Error: " + msg, "ERROR");
});

// Start casper js
casper.start(url, function() {

     this.evaluate(function evaluateStuffAfterStart(ip) {
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
    
});

casper.then(function() {
    var info = this.evaluate(function evaluateStuffAfterStart() {
        text= document.querySelector("pre").textContent;
        return text;
    });
    console.log(info);
});


casper.run();
