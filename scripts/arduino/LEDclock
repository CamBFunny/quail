#include "Arduino.h"
#include "uRTCLib.h"

// uRTCLib rtc;
uRTCLib rtc(0x68);

char daysOfTheWeek[12][4] = { "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" };


// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  Serial.begin(9600);

  URTCLIB_WIRE.begin();

  // Comment out below line once you set the date & time.
  // Following line sets the RTC with an explicit date & time
  // // for example to set April 14 2025 at 12:56 you would call:
  // rtc.set(0, 58, 21, 7, 22, 8, 25);
  // rtc.set(second, minute, hour, dayOfWeek, dayOfMonth, month, year)
  // set day of week (1=Sunday, 7=Saturday)


  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Cam's ArduinoUno");
  String minute_string = String(10); 
  String seconds_string = String(10);
}

void loop() {
  rtc.refresh(); 
  int year = rtc.year();
  String check = daysOfTheWeek[rtc.month() - 1]; 
  String month = check;

  int day = rtc.day(); 
  int hour = rtc.hour(); 

  int minutes = rtc.minute();  
  String minutes_string = String(minutes);
  if (minutes < 10) {
    minutes_string = "0" + String(minutes);
  }    

  int seconds = rtc.second(); 
  String seconds_string = String(seconds);
  if (seconds < 10) {
    seconds_string = "0" + String(seconds);
  }  
  
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1); 
  String colon = ":";
  String dash = "-";
  lcd.print(hour + colon + minutes_string + colon + seconds_string + " " + month + dash + day + "   ");

  delay(500);

}
