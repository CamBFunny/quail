#include <SPI.h>
#include "epd4in2_V2.h"
#include "imagedata.h"
#include "epdpaint.h"

#define COLORED     0
#define UNCOLORED   1

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Epd epd;

  if (epd.Init() != 0) {
    Serial.print("e-Paper init failed");
    return;
  }
	//Serial.print(UNCOLORED);
  /* This clears the SRAM of the e-paper display */
  epd.Clear();

#if 0

  /**
    * Due to RAM not enough in Arduino UNO, a frame buffer is not allowed.
    * In this case, a smaller image buffer is allocated and you have to 
    * update a partial display several times.
    * 1 byte = 8 pixels, therefore you have to set 8*N pixels at a time.
    */
  unsigned char image[1500];
  Paint paint(image, 400, 28);    //width should be the multiple of 8 
  sleep(3);

  paint.Clear(UNCOLORED);
  paint.DrawStringAt(20, 5, "e-Paper Demo", &Font16, COLORED);
  epd.Display_Partial_Not_refresh(paint.GetImage(), 0, 32, 0+paint.GetWidth(), 32+paint.GetHeight());
 
  paint.Clear(COLORED);
  paint.DrawStringAt(20, 5, "Hello world!", &Font16, UNCOLORED);
  epd.Display_Partial_Not_refresh(paint.GetImage(), 0, 64, 0+paint.GetWidth(), 64+paint.GetHeight());
  sleep(3);
  
  paint.SetWidth(64);
  paint.SetHeight(64);
  sleep(3);
  
  paint.Clear(UNCOLORED);
  paint.DrawRectangle(0, 0, 40, 50, COLORED);
  paint.DrawLine(0, 0, 40, 50, COLORED);
  paint.DrawLine(40, 0, 0, 50, COLORED);
  epd.Display_Partial_Not_refresh(paint.GetImage(), 10, 130, 10+paint.GetWidth(), 130+paint.GetHeight());

  paint.Clear(UNCOLORED);
  paint.DrawCircle(32, 32, 30, COLORED);
  epd.Display_Partial_Not_refresh(paint.GetImage(), 90, 120, 90+paint.GetWidth(), 120+paint.GetHeight());

  paint.Clear(UNCOLORED);
  paint.DrawFilledRectangle(0, 0, 40, 50, COLORED);
  epd.Display_Partial_Not_refresh(paint.GetImage(), 10, 200, 10+paint.GetWidth(), 200+paint.GetHeight());

  paint.Clear(UNCOLORED);
  paint.DrawFilledCircle(32, 32, 30, COLORED);
  epd.Display_Partial(paint.GetImage(), 90, 190, 90+paint.GetWidth(), 190+paint.GetHeight());


  /* This displays an image */
  epd.Init();
  Serial.print("show 2-gray image\r\n");
  epd.Display(IMAGE_BUTTERFLY);
  delay(1000);

#else

  Serial.print("show 4-gray image\r\n");
  epd.Init_4Gray();
  epd.Set_4GrayDisplay(gImage_4in2_4Gray1, 100, 100, 200, 150);

#endif

  /* Deep sleep */
  epd.Sleep();

}

void loop() {

}
