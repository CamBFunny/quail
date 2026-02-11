#include <iostream>
#include <chrono>
#include <thread> // Included for the sleep function in the example
#include <unistd.h> // in linux: sleep()

int main() {
    // Record the time point when the program starts
    auto program_start_time = std::chrono::high_resolution_clock::now();
    int delta_time = 0;
    int ms = 0;
    int seconds = 0;
    int minutes = 0;
    int hours = 0;
    int reference_frame = 0;

    while (true) {

    // --- Your program's code goes here ---
    system("clear");
    std::cout << "Program running...\n";
    // Capture the current time
    auto current_time = std::chrono::high_resolution_clock::now();

    // Calculate the duration elapsed since the program started
    auto duration = current_time - program_start_time;

    // Cast the duration to milliseconds and get the count
    auto milliseconds_since_start = std::chrono::duration_cast<std::chrono::milliseconds>(duration).count();

    // Convert to milliseconds and store as integer (long long recommended)
    long long milli = std::chrono::duration_cast<std::chrono::milliseconds>(duration).count();
    delta_time = milli - reference_frame;
    reference_frame = milli;
    ms = ms + delta_time;

    if (ms >= 1000) {
        seconds++;
        ms = ms - 1000;
    }

    if (seconds >= 60) {
        minutes++;
        seconds = seconds - 60;
    }

    if (minutes >= 60) {
        hours++;
        minutes = minutes - 60;
    }

    if (hours > 0) {
        printf("%d:", hours);
        if (minutes < 10) {
            printf("0%d:", minutes);
        } else {
            printf("%d:", minutes);
        }
        if (seconds >= 10) {
            printf("%d.", seconds);
        } else {
            printf("0%d.", seconds);
        }
    } else {
        if (seconds >= 10) {
            printf("%d:%d.", minutes, seconds);
        } else {
            printf("%d:0%d.", minutes, seconds);
        }
    }

    if (ms < 10) {
        printf("00%d\n", ms);
    } else if (10 <= ms && ms < 100) {
        printf("0%d\n", ms);
    } else {
        printf("%d\n", ms);
    }

    // Simulate time passing
    std::this_thread::sleep_for(std::chrono::milliseconds(50));
    }
}
