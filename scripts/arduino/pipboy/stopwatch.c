#include <iostream>
#include <unistd.h> // in linux: sleep()

// #include <windows.h> // in windows: Sleep()


using namespace std;

void displayTime(int hours, int minutes, int seconds) {
   // for linux
   system("clear"); 

   // for windows
   // system("cls");

   cout << hours << ":"
        << minutes << ":"
        << seconds << endl;
}

int main() {
  int hour = 0;
  int min = 0;
  int sec = 0;

  displayTime(hour, min, sec);

  while(true) {
    sleep(1);

    sec++;

    if(sec > 59) {
      min++;
      sec = 0;
    } 

    if(min > 59) {
      hour++;
      sec = 0;
      min = 0;
    }

    displayTime(hour, min, sec);
  }
}
