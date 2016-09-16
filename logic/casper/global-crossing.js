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
  //  logLevel: "debug",              // Only "info" level messages will be logged
  //  verbose: true                  // log messages will be printed out to the console
});

/*
 * Necesary variables
 */
var utils = require('utils');
var ip = casper.cli.get('addr');
var router = casper.cli.get('router');

/*
 * URL for extrac information
 */
var url = 'http://ipstats.globalcrossing.net/cgi-bin/lg/lg.cgi?lgCall=r2htrace';

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
    this.evaluate(function evaluateStuffAfterStart(ip, router) {

        options = document.getElementsByTagName('option');
        
        //Select the source router
        for(var i=0; i<options.length; i++){
            if(options[i].value==router){
                document.getElementsByTagName('option')[i].selected = 'selected';
            }
        }
        
        
        //Select the input
        input = document.getElementsByName("destAddress")[0] ;
        //Change the address
        input.value = ip;
        //Submit the form
        submit = document.getElementsByTagName("input")[3];
        submit.click();        
    }, ip, router);
     casper.capture('main.png');   
});

/*
 * Execute some code after load the page
 */
casper.then(function() {
    casper.capture('content.png');
    var info = this.evaluate(function evaluateStuffAfterStart() {
        text= document.querySelector("pre").textContent;
        return text;
    });
    console.log(info);
});


casper.run();
