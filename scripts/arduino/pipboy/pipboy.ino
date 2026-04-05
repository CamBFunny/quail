/*
 * Created by ArduinoGetStarted.com
 *
 */

#include <DIYables_TFT_Round.h>
#include <math.h>
#include "bitmap.h"

// REAL-TIME CHIP
#include <SPI.h>
#include <Wire.h>
#include "uRTCLib.h"
// uRTCLib rtc;
uRTCLib rtc(0x68);
char daysOfTheWeek[12][4] = { "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" };

#define WHITE     DIYables_TFT::colorRGB(255, 255, 255)

#define PIN_RST 8 // The Arduino pin connected to the RST pin of the circular TFT display
#define PIN_DC  9 // The Arduino pin connected to the DC pin of the circular TFT display
#define PIN_CS 10 // The Arduino pin connected to the CS pin of the circular TFT display

#define CLR_BLACK DIYables_TFT::colorRGB(0, 0, 0)  // Black
#define CLR_WHITE DIYables_TFT::colorRGB(255, 255, 255) // White
#define CLR_RED DIYables_TFT::colorRGB(255, 80, 80)    // Red-ish
#define CLR_GREEN DIYables_TFT::colorRGB(80, 255, 80)  // Green-ish
#define CLR_BLUE DIYables_TFT::colorRGB(0, 0, 255)    // Blue
#define CLR_PINK DIYables_TFT::colorRGB(255, 125, 180)    // Pink
#define CLR_GOLD DIYables_TFT::colorRGB(240, 200, 0)    // Gold

// Rachel's pick
#define CLR_DARKBLUE DIYables_TFT::colorRGB(10, 30, 40)  
#define CLR_LIGHTBLUE DIYables_TFT::colorRGB(40, 110, 210)
#define CLR_GOLD DIYables_TFT::colorRGB(240, 200, 0)    // Gold

#define COLOR_HOUR CLR_LIGHTBLUE
#define COLOR_MINUTE CLR_LIGHTBLUE
#define COLOR_SECOND CLR_WHITE

#define COLOR_BACKGROUND CLR_DARKBLUE
#define COLOR_TICKS CLR_LIGHTBLUE


DIYables_TFT_GC9A01_Round TFT_display(PIN_RST, PIN_DC, PIN_CS);


uint16_t SCREEN_WIDTH;
uint16_t SCREEN_HEIGHT;

// Watch dimensions
const int CENTER_X = 120;
const int CENTER_Y = 120;
const int RADIUS = 115;
const int HOUR_LEN = 35;
const int MIN_LEN = 52;
const int SEC_LEN = 62;

float prevHourAngle = -1000, prevMinAngle = -1000, prevSecAngle = -1000;
int prevDispHour = -1, prevDispMin = -1, prevDispSec = -1;

void drawHand(int x, int y, float angle, int length, uint16_t color, int width) {
  int x2 = x + length * cos(angle - M_PI / 2);
  int y2 = y + length * sin(angle - M_PI / 2);
  for (int w = -width / 2; w <= width / 2; w++) {
    TFT_display.drawLine(x + w, y + w, x2 + w, y2 + w, color);
  }
}

void drawTicks() {
  for (int i = 0; i < 60; i++) {
    float angle = i * 6 * M_PI / 180.0;
    int x1 = CENTER_X + (RADIUS - 8) * cos(angle - M_PI / 2);
    int y1 = CENTER_Y + (RADIUS - 8) * sin(angle - M_PI / 2);
    int x2 = CENTER_X + (RADIUS - (i % 5 == 0 ? 22 : 14)) * cos(angle - M_PI / 2);
    int y2 = CENTER_Y + (RADIUS - (i % 5 == 0 ? 22 : 14)) * sin(angle - M_PI / 2);
    TFT_display.drawLine(x1, y1, x2, y2, COLOR_TICKS);
  }
  TFT_display.setTextColor(COLOR_TICKS, COLOR_BACKGROUND);
  TFT_display.setTextSize(2);
  for (int h = 1; h <= 12; h++) {
    // Watch number positions
    float angle = (h * 30) * M_PI / 180.0;
    int tx = CENTER_X + (RADIUS - 38) * cos(angle - M_PI / 2) - 10;
    int ty = CENTER_Y + (RADIUS - 38) * sin(angle - M_PI / 2) - 8;
    if (h == 3) {
      tx = tx + 10;
      ty = ty + 1;
    }
    if (h == 2 || h == 4) {
      tx = tx + 7;
    }
    if (h == 1 || h == 5 || h == 6 || h == 7 || h == 8) {
      tx = tx + 5;
    }
    if (h == 9) {
      ty = ty + 1;
    }
    TFT_display.setCursor(tx, ty);
    TFT_display.print(h);
  }
}

void printTime(int previous, int now, const char* offset, bool colon = true) {
  int16_t x = 70, y = 200;
  int16_t x1, y1;
  uint16_t w, h;
  TFT_display.getTextBounds(offset, x, y, &x1, &y1, &w, &h);

  // Update digital display
  TFT_display.setCursor(x + w, y);
  TFT_display.print("  ");
  TFT_display.setCursor(x + w, y);

  if (now < 10)
    TFT_display.print('0');

  TFT_display.print(now);

  if (colon)
    TFT_display.print(":");
}

void setup() {
  Serial.begin(9600); 
  TFT_display.begin();

  // Splash screen
  SCREEN_WIDTH = TFT_display.width();
  SCREEN_HEIGHT = TFT_display.height();

  int img_width = 120;
  int img_height = 53;
  
  int x = (SCREEN_WIDTH - img_width) / 2;
  int y = (SCREEN_HEIGHT - img_height) / 2;

  // TFT_display.fillScreen(WHITE);
  // TFT_display.drawRGBBitmap(x, y, myBitmap, img_width, img_height); 
  // delay(1000);
  
  TFT_display.fillScreen(COLOR_BACKGROUND);

  char style[] = "analogue"; 
  if (strcmp(style, "analogue") == 0) {
    TFT_display.drawCircle(CENTER_X, CENTER_Y, RADIUS, COLOR_TICKS);
    drawTicks();
  }

  TFT_display.setTextColor(DIYables_TFT::colorRGB(255, 255, 0), COLOR_TICKS);
  TFT_display.setTextSize(2);

  // Ensure first update in loop() repaints everything
  prevDispHour = -1;
  prevDispMin = -1;
  prevDispSec = -1;

  // Clock setup
  URTCLIB_WIRE.begin();
  // rtc.set(7, 57, 14, 6, 3, 4, 26);
  // rtc.set(second, minute, hour, dayOfWeek, dayOfMonth, month, year)
  // set day of week (1=Sunday, 7=Saturday)
  
}

void loop() {
  // Check time
  rtc.refresh();
  int year = rtc.year();
  String check = daysOfTheWeek[rtc.month() - 1];
  String month = check;

  int day = rtc.day();
  int hours = rtc.hour();
  if (hours > 12) {
    hours -= 12;
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
   

  if (minutes >= 0 && minutes <= 60 && day <= 31 && year < 30) {
    float sec = fmod(seconds, 60.0);
    float min = fmod(minutes, 60.0);
    float hour = fmod(hours, 12.0);
  
    int dispHour = (int)hour == 0 ? 12 : (int)hour;
    int dispMin = (int)min;
    int dispSec = (int)sec;
  
    float hourAngle = (hour + min / 60.0) * 30 * M_PI / 180.0;
    float minAngle = (min + sec / 60.0) * 6 * M_PI / 180.0;
    float secAngle = sec * 6 * M_PI / 180.0;  
      
    // Minute hand (jumps)
    if (dispMin != prevDispMin) { 
      if (prevMinAngle > -900)
        for (int h = 1; h <= 50; h++) {
          float wave = (min + (sec - h) / 60.0) * 6 * M_PI / 180.0;
          drawHand(CENTER_X, CENTER_Y, wave, MIN_LEN, COLOR_BACKGROUND, 2);  // clear old position
        }
      drawHand(CENTER_X, CENTER_Y, minAngle, MIN_LEN, COLOR_MINUTE, 2);
      
      prevDispMin = dispMin;
      prevMinAngle = minAngle;
      
      Serial.print("Current Date & Time: ");
      Serial.print(day);
      Serial.print('/');
      Serial.print(rtc.month());
      Serial.print('/');
      Serial.print(rtc.year());
    
      Serial.print(" (");
      Serial.print(daysOfTheWeek[rtc.dayOfWeek() - 1]);
      Serial.print(") ");
    
      Serial.print(rtc.hour());
      Serial.print(':');
      int minute = rtc.minute(); 
      if (minute < 10) {
        Serial.print("0");
      } 
      Serial.print(minute);
      Serial.print(':');
      int number = rtc.second(); 
      if (number < 10) {
        Serial.print("0");
      } 
      Serial.println(number);
    }
    
    // Hour hand (jumps), redraw when angle changed
    if (dispHour != prevDispHour) {
      if (prevHourAngle > -900)
        drawHand(CENTER_X, CENTER_Y, prevHourAngle, HOUR_LEN, COLOR_BACKGROUND, 3);  // clear old position
      drawHand(CENTER_X, CENTER_Y, hourAngle, HOUR_LEN, COLOR_HOUR, 3);
      
      prevHourAngle = hourAngle;
      prevDispHour = dispHour;
    }
  
    if (dispSec - (dispHour%12)*5 == 9 || seconds == 0) {
      drawHand(CENTER_X, CENTER_Y, hourAngle, HOUR_LEN, COLOR_HOUR, 3);
    }
  
    if (dispSec - dispMin == 3 || seconds == 0) {
      drawHand(CENTER_X, CENTER_Y, minAngle, MIN_LEN, COLOR_MINUTE, 2);
    }
  
    // Second hand (smooth)
    if (dispSec != prevDispSec) {
      if (prevSecAngle > -900)
        drawHand(CENTER_X, CENTER_Y, prevSecAngle, SEC_LEN, COLOR_BACKGROUND, 1);  // clear old position
  
      drawHand(CENTER_X, CENTER_Y, secAngle, SEC_LEN, COLOR_SECOND, 1);
      TFT_display.fillCircle(CENTER_X, CENTER_Y, 4, COLOR_SECOND);  // Redraw center dot
  
      prevDispSec = dispSec;
      prevSecAngle = secAngle;
    }
  }
  else {
    Serial.println("Missed bits!!!!!!!!"); 
  }
  

  delay(50);
}
