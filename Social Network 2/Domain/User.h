
#pragma once
#include <iostream>
#include <string>
using namespace std;

class User {
private:
    int id;
    string name;
public:
    User();
    ///constructorul va initializa datele membru

    User(int, string);
    ///constructorul de atribuire

    User(const User&);
    ///constructorul de copiere


    string getName();
    ///returneaza numele

    int getId();
    ///returneaza id-ul

    void setName(string);
    ///seteaza numele cu stringul dat de utilizator

    void setId(int);
    ///seteaza id-ul cu int-ul dat de utilizator


    User& operator = (const User&);
    ///operatorul de atribuire

    bool operator == (const User&);
    ///opreatorul de egalitate

    bool operator != (const User&);
    ///operatorul de diferentiere

    bool operator > (const User&);
    ///operatorul de "mai mare"

    bool operator < (const User&);
    ///operatorul de "mai mic"

    friend ostream& operator<<(ostream&, User&);
    ///suprascriere pentru afisare

    friend istream& operator>>(istream& , User&);
    ///suprascriere pentru citire

    ~User();
    ///destructor
};