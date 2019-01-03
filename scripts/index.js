var Blynk = require("blynk-library");


var sense = require("node-sense-hat");

var imu = sense.Imu;
var IMU = new imu.IMU();
var AUTH = "23c74f29e4d341db8f3c4d2b44ff7f81";

var blynk = new Blynk.Blynk(AUTH);

//declare use of sensor pins
var v1 = new blynk.VirtualPin(1);

var v3 = new blynk.VirtualPin(3);

//remote light switch

var white = [255, 255, 255];
sense.Leds.clear();

v1.on('write', function(param) {
  console.log('V1:', param[0]);
  if(param[0]==1){
    sense.Leds.clear(white)
    }else{
	sense.Leds.clear();
	}
});


//remote environment light sensor

v3.on('write', function(param) {
//check if it's too dark
if (param[0]<80){console.log("It's a bit dark, mate")
	
	}else{
	
}
});

