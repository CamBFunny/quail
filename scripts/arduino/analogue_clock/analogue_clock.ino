/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-round-circular-tft-lcd-display
 */

#include <DIYables_TFT_Round.h>
#include <math.h>
#include "bitmap.h"

#define WHITE     DIYables_TFT::colorRGB(255, 255, 255)

#define PIN_RST 8 // The Arduino pin connected to the RST pin of the circular TFT display
#define PIN_DC  9 // The Arduino pin connected to the DC pin of the circular TFT display
#define PIN_CS 10 // The Arduino pin connected to the CS pin of the circular TFT display

#define COLOR_BACKGROUND DIYables_TFT::colorRGB(0, 0, 0)  // Black
#define COLOR_HOUR DIYables_TFT::colorRGB(255, 80, 80)    // Red-ish
#define COLOR_MINUTE DIYables_TFT::colorRGB(80, 255, 80)  // Green-ish
#define COLOR_SECOND DIYables_TFT::colorRGB(0, 0, 255)    // Blue
#define CLR_PINK DIYables_TFT::colorRGB(255, 125, 180)    // Pink
#define CLR_GOLD DIYables_TFT::colorRGB(240, 200, 0)    // Gold

#define COLOR_USED CLR_GOLD

DIYables_TFT_GC9A01_Round TFT_display(PIN_RST, PIN_DC, PIN_CS);


int img_width = 120;
int img_height = 53;

uint16_t SCREEN_WIDTH;
uint16_t SCREEN_HEIGHT;


const int CENTER_X = 120;
const int CENTER_Y = 120;
const int RADIUS = 110;
const int HOUR_LEN = 40;
const int MIN_LEN = 50;
const int SEC_LEN = 60;

const unsigned long PRESET_MS =
  6UL * 3600000UL +  //  9 hours
  32UL * 60000UL +    //  0 minutes
  29UL * 1000UL;      //  5 seconds

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
    TFT_display.drawLine(x1, y1, x2, y2, COLOR_USED);
  }
  TFT_display.setTextColor(COLOR_USED, COLOR_BACKGROUND);
  TFT_display.setTextSize(2);
  for (int h = 1; h <= 12; h++) {
    float angle = (h * 30) * M_PI / 180.0;
    int tx = CENTER_X + (RADIUS - 38) * cos(angle - M_PI / 2) - 10;
    int ty = CENTER_Y + (RADIUS - 38) * sin(angle - M_PI / 2) - 8;
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

  SCREEN_WIDTH = TFT_display.width();
  SCREEN_HEIGHT = TFT_display.height();

  int x = (SCREEN_WIDTH - img_width) / 2;
  int y = (SCREEN_HEIGHT - img_height) / 2;

  TFT_display.fillScreen(WHITE);
  TFT_display.drawRGBBitmap(x, y, myBitmap, img_width, img_height);
  
  delay(2000); 
  
  TFT_display.fillScreen(COLOR_BACKGROUND);
  TFT_display.drawCircle(CENTER_X, CENTER_Y, RADIUS, COLOR_USED);
  drawTicks();

  TFT_display.setTextColor(DIYables_TFT::colorRGB(255, 255, 0), COLOR_BACKGROUND);
  TFT_display.setTextSize(2);

  // Ensure first update in loop() repaints everything
  prevDispHour = -1;
  prevDispMin = -1;
  prevDispSec = -1;
}

void loop() {
  // Add preset offset to millis()
  unsigned long ms = millis() + PRESET_MS;

  float sec = fmod(ms / 1000.0, 60.0);
  float min = fmod(ms / 60000.0, 60.0);
  float hour = fmod(ms / 3600000.0, 12.0);

  int dispHour = (int)hour == 0 ? 12 : (int)hour;
  int dispMin = (int)min;
  int dispSec = (int)sec;

  float hourAngle = (hour + min / 60.0) * 30 * M_PI / 180.0;
  float minAngle = (min + sec / 60.0) * 6 * M_PI / 180.0;
  float secAngle = sec * 6 * M_PI / 180.0;

  // Hour hand (jumps), redraw when angle changed
  if (dispHour != prevDispHour || dispMin != prevDispMin) {
    if (prevHourAngle > -900)
      drawHand(CENTER_X, CENTER_Y, prevHourAngle, HOUR_LEN, COLOR_BACKGROUND, 7);  // clear old position
    drawHand(CENTER_X, CENTER_Y, hourAngle, HOUR_LEN, COLOR_HOUR, 7);
    prevHourAngle = hourAngle;

    // Update digital display
    if (dispHour != prevDispHour) {
      prevDispHour = dispHour;
    }
  }

  if (dispSec - (dispHour%12)*5 == 9) {
    if (prevHourAngle > -900)
      drawHand(CENTER_X, CENTER_Y, prevHourAngle, HOUR_LEN, COLOR_BACKGROUND, 7);  // clear old position
    drawHand(CENTER_X, CENTER_Y, hourAngle, HOUR_LEN, COLOR_HOUR, 7);
  }

  if (dispSec - dispMin == 3) {
    if (prevMinAngle > -900)
      drawHand(CENTER_X, CENTER_Y, prevMinAngle, MIN_LEN, COLOR_BACKGROUND, 5);  // clear old position
    drawHand(CENTER_X, CENTER_Y, minAngle, MIN_LEN, COLOR_MINUTE, 5);
  }

  // Minute hand (jumps)
  if (dispMin != prevDispMin) {
    if (prevMinAngle > -900)
      drawHand(CENTER_X, CENTER_Y, prevMinAngle, MIN_LEN, COLOR_BACKGROUND, 5);  // clear old position
    drawHand(CENTER_X, CENTER_Y, minAngle, MIN_LEN, COLOR_MINUTE, 5);

    prevDispMin = dispMin;
    prevMinAngle = minAngle;
  }

  // Second hand (smooth)
  if (dispSec != prevDispSec) {
    if (prevSecAngle > -900)
      drawHand(CENTER_X, CENTER_Y, prevSecAngle, SEC_LEN, COLOR_BACKGROUND, 2);  // clear old position

    drawHand(CENTER_X, CENTER_Y, secAngle, SEC_LEN, COLOR_SECOND, 2);
    TFT_display.fillCircle(CENTER_X, CENTER_Y, 7, COLOR_SECOND);  // Redraw center dot

    // Update digital display
    prevDispSec = dispSec;
    prevSecAngle = secAngle;
  }
}
