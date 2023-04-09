#pragma once
#include <string>


using namespace std;

class Friendship{
private:
    string name1;
    string name2;
public:
    Friendship();
    ///constructorul va initializa datele membru

    Friendship(string , string);
    ///constructorul de atribuire

    Friendship(const Friendship&);
    ///constructorul de copiere

    string getName1();
    ///returneaza primul nume

    string getName2();
    ///returneaza al doilea nume

    void setName1(string);
    ///seteaza primul nume cu stringul dat de utilizator

    void setName2(string);
    ///seteaza al doilea nume cu stringul dat de utilizator

    Friendship& operator = (const Friendship&);
    ///operatorul de atribuire

    bool operator == (const Friendship&);
    ///opreatorul de egalitate

    bool operator != (const Friendship&);
    ///operatorul de diferentiere

    ~Friendship();
    ///destructorul
};
