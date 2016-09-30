/**
 *Daniel Santos
 *september, 2016
 */

/*
 * Inital configuration 
 */
var casper = require('casper').create({
    pageSettings: {
        loadImages:  false,        
        loadPlugins: false         
    },
//    logLevel: "debug",              // Only "info" level messages will be logged
//    verbose: true                  // log messages will be printed out to the console
});


var fs=require('fs');
/*
 * Necesary variables
 */
var utils = require('utils');
var ip = casper.cli.get('addr');
var router = casper.cli.get('router');

/*
 * URL for extrac information
 */
var url = 'http://lg.eastlink.ca/';

/*
 *print out all the messages in the headless browser context
 */
casper.on('remote.message', function(msg) {
    this.echo('remote message caught: ' + msg);
});

/*
 *print out all the messages in the headless browser context
 */
casper.on("page.error", function(msg, trace) {
    this.echo("Page Error: " + msg, "ERROR");
});


/*
 * Start casper js
 */
casper.start(url, function() {
    console.log(ip);
    this.evaluate(function evaluateStuffAfterStart(ip, router) {

        document.getElementsByTagName('option')[2].selected = 'selected';
        document.getElementsByName("addr")[0].value = ip;
        document.getElementsByTagName("input")[5].checked = true;
        submit = document.getElementsByTagName("input")[7];
        submit.click();        
    }, ip, router);
     //casper.capture('eas.png');  
});

/*
 * Execute some code after load the page
 */
casper.then(function() {
    this.wait(2000, function() {
      //  fs.write("result-east.html", this.getHTML() );
    });
    var info = this.evaluate(function evaluateStuffAfterStart() {
        text= document.querySelector("pre").textContent;
        return text;
    });
    console.log(info);
    
   // console.log(this.getHTML())
});


casper.run();
