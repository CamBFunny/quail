// OLED SCREEN
#include "Arduino.h"
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define OLED_RESET -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C
int duration = 9000;

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// REAL-TIME CHIP
#include "uRTCLib.h"
// uRTCLib rtc;
uRTCLib rtc(0x68);

char daysOfTheWeek[12][4] = { "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" };

void setup() {
  Serial.begin(9600);

  URTCLIB_WIRE.begin();

  // set day of week (1=Sunday, 7=Saturday) 
  // (sec, min, hour, dayofweek, dayofmonth, month, year)
  // Comment out below line once you set the date & time.
  // rtc.set(7, 43, 15, 1, 8, 2, 26);
  
  Serial.begin(9600);
  
  // Initialize the OLED object
  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
  Serial.println(F("SSD1306 allocation failed"));
  }
  
  // Clear the buffer
  display.clearDisplay();
  // Display Text
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setTextWrap(false);
  display.setCursor(34, 1);
  display.println("Cam's");
  display.setCursor(28, 17);
  display.println("Pipboy"); 
  display.invertDisplay(true);
  display.display();
  delay(1800);
  display.invertDisplay(false);
}

void loop() {
  rtc.refresh(); 
  int year = rtc.year();
  String check = daysOfTheWeek[rtc.month() - 1]; 
  String month = check;

  int day = rtc.day(); 
  int hour = rtc.hour(); 
  if (hour > 12) {
    hour -= 12;
  }

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
   
  String colon = ":";
  String dash = "-";
  
  display.clearDisplay();  
  display.setCursor(7, 2);
  display.setTextSize(1);
  display.println("Time");
  display.setCursor(70, 1);
  if (day > 9) {
    display.setCursor(58, 1);
  }
  display.setTextSize(2);
  display.println(month + dash + day + "   ");
  
  int x = 12;
  int y = 28;
  int adjust = 0;
  if (hour > 9) {
    adjust = adjust + 9;
  }
  display.setCursor(x - adjust, y);
  display.setTextSize(3);
  display.print(hour + colon + minutes_string);
  display.setTextSize(2);
  display.setCursor(x + 72 + adjust, y + 7);
  display.println(colon + seconds_string);
  display.display();
  delay(250);

} 
