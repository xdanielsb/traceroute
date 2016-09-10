//Inital configuration for casper js
var casper = require('casper').create({
    pageSettings: {
        loadImages:  false,        // The WebPage instance used by Casper will
        loadPlugins: false         // use these settings
    },
    logLevel: "debug",              // Only "info" level messages will be logged
    verbose: true                  // log messages will be printed out to the console
});
var utils = require('utils');
var ip = casper.cli.get('addr');


//Initial parameters for casper js
var url = 'http://ipstats.globalcrossing.net/cgi-bin/lg/lg.cgi?lgCall=r2htrace';

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
     casper.capture('main.png');   
});

casper.then(function() {
    casper.capture('content.png');
    var info = this.evaluate(function evaluateStuffAfterStart() {
        text= document.querySelector("pre").textContent;
        return text;
    });
    console.log(info);
});


casper.run();
