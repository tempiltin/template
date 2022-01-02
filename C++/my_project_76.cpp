#include <iostream>
#include <ctime>
using namespace std;
int main() {
    time_t now = time(0);
    tm *ltm = localtime(&now);
    cout << "Time: " << 1 + ltm->tm_hour << ":" 
         << 1 + ltm->tm_min << ":" 
         << 1 + ltm->tm_sec << endl;
    return 0;
}