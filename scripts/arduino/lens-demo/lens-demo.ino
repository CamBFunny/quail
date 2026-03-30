#include <U8g2lib.h>
#include "images.h"

U8G2_SSD1309_128X64_NONAME0_F_4W_SW_SPI display(
  U8G2_R0,
  /* clock=*/13,
  /* data=*/11,
  /* cs=*/10,
  /* dc*/9,
  /* reset=*/8
  );

int split = 1200;
int counter = 0;

void setup() {
  // put your setup code here, to run once:
  display.begin(); 
}

void loop() {
  // put your main code here, to run repeatedly:
  if (counter < 1) {
  display.setFont(u8g2_font_6x12_tf);
  display.drawStr(0, 14, "Hello, world!");

  display.sendBuffer();
  delay(split);
  display.clearBuffer();

  display.setFontMode(1);  /* activate transparent font mode */
  display.setDrawColor(1); /* color 1 for the box */
  display.drawBox(22, 2, 55, 50);
  display.setFont(u8g2_font_ncenB10_tf);
  display.setDrawColor(0);
  display.drawStr(5, 18, "Dark");
  display.setDrawColor(1);
  display.drawStr(5, 33, "Light");
  display.setDrawColor(2);
  display.drawStr(5, 48, "Dynamic");
  // Reset 
  display.setDrawColor(1); 
  display.setFont(u8g2_font_6x10_tf);
  display.sendBuffer();
  delay(split);
  display.clearBuffer();

  // Draw rectangle
  display.setCursor(0, 9);
  display.println("Rectangle");
  display.drawFrame(10,20,25,15);
  display.sendBuffer();
  delay(split);
  display.clearBuffer();

  // Draw Snowman
  display.setFont(u8g2_font_unifont_t_symbols);
  display.drawUTF8(5, 20, "Snowman: ☃");  
  display.setFont(u8g2_font_6x10_tf);  // Reset
  display.sendBuffer();
  delay(split);
  display.clearBuffer();

  // Draw empty circle
  display.setCursor(0, 14);
  display.println("Circle");
  display.drawCircle(20, 35, 10, 15);
  display.sendBuffer();
  delay(split);
  display.clearBuffer();
    
  // Draw filled circle
  display.setCursor(0, 14);
  display.println("Filled Circle (Disk)");
  display.drawDisc(20, 35, 10, 15);
  display.sendBuffer();
  delay(split);
  display.clearBuffer();

  // Draw triangle
  display.setCursor(0, 14);
  display.println("Triangle");
  display.drawTriangle(30, 15, 0, 60, 60, 60);
  display.sendBuffer();
  delay(split);
  display.clearBuffer();
  }
  
  display.drawXBMP( 0, 0, 128, 64, epd_bitmap_allArray[counter]);
  display.sendBuffer();
  delay(split);
  display.clearBuffer();
  counter++;
  if (counter >= 16) {counter = 0;}
}
