#include <iostream>
#include <chrono>
#include <thread> // Included for the sleep function in the example
#include <unistd.h> // in linux: sleep()

int main() {
    // Record the time point when the program starts
    auto program_start_time = std::chrono::high_resolution_clock::now();
    int delta_time = 0;
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
    long long ms = std::chrono::duration_cast<std::chrono::milliseconds>(duration).count(); 
    int delta_time = ms - reference_frame;
    
    printf("%d\n", ms);
    if (ms >= 1000);
    
    std::cout << "Time since program started: " << milliseconds_since_start << " milliseconds." << std::endl;
    
    // Simulate time passing
    std::this_thread::sleep_for(std::chrono::milliseconds(1000));
    }
}
