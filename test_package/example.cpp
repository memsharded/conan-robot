#include "Timer.h"
#include <iostream>

using namespace Robot;

int main (void){
    Timer t1;
    std::cout<<!t1.HasStarted()<<"\n";
	std::cout << "CPU Time: " << Timer::GetCpuTime() << "\n";
    return 0;
}