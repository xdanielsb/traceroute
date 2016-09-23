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
 //   logLevel: "debug",              // Only "info" level messages will be logged
 //   verbose: true                  // log messages will be printed out to the console
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
var url = 'http://lg.teleglobe.net/bin/lg.cgi';

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

        //Select the ipv4 option
        document.getElementsByName("addr")[0].value = "216.58.192.68"
//        document.getElementsByTagName('option')[3].selected = 'selected'
        submit = document.getElementsByTagName("input")[4]
        submit.click();        
    }, ip, router);
    // casper.capture('main2.png');   
});

/*
 * Execute some code after load the page
 */
casper.then(function() {
   /* this.wait(2000, function() {
        fs.write("result-teleglobe.html", this.getHTML() );
    });*/
   //casper.capture('content2.png');
    var info = this.evaluate(function evaluateStuffAfterStart() {
        text= document.querySelector("PRE").textContent;
        return text;
    });
    //fs.write("result-teleglobe.html", info );
    console.log(info);
});


casper.run();
