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

void setup() {
Serial.begin(9600);

// Initialize the OLED object
if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
Serial.println(F("SSD1306 allocation failed"));
}

// Clear the buffer
display.clearDisplay();

// Display Text
display.setTextSize(1);
display.setTextColor(WHITE);
display.setTextWrap(false);
display.setCursor(0, 28);
display.println("Hello world!");
display.display();
delay(1000);
display.setCursor(0, 0);
display.clearDisplay();
// Scroll full screen
display.setTextSize(1);
display.println("Full");
display.println("screen");
display.println("scrolling!");
display.println("~~~~~~~~~~~");
display.println("123456789012345678901");
display.println("~Hello world!~");
display.println("This is a test loop.");
display.display();
}

void loop() {
display.startscrollleft(0x00, 0x07);
delay(duration);
display.stopscroll();
delay(1000);
display.startscrollright(0x00, 0x07);
delay(duration);
display.stopscroll();
delay(1000);
}
