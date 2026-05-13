#include <iostream>
using namespace std;

int main() {
    int numStudents;
    cout << "Enter number of students: ";
    cin >> numStudents;

    string name;
    float grade, total = 0;

    for (int i = 0; i < numStudents; i++) {
        cout << "Enter student name: ";
        cin >> name;

        cout << "Enter grade: ";
        cin >> grade;

        total += grade;
    }

    float average = total / numStudents;

    cout << "Average grade: " << average << endl;

    return 0;
}