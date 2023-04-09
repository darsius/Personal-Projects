#pragma once
#include <string>

using namespace std;

class Message{
private:
    string name1;
    string name2;
    string text;
public:
    Message();
    ///constructorul va initializa datele membru

    Message(string, string, string);
    ///constructorul de atribuire

    Message(const Message&);
    ///constructorul de copiere

    string getName1();
    ///returneaza primul nume

    string getName2();
    ///returneaza al doilea nume

    string getText();
    ///returneaza mesajul dintre useri.

    void setName1(string);
    ///seteaza primul nume cu stringul dat de utilizator

    void setName2(string);
    ///seteaza al doilea nume cu stringul dat de utilizator

    void setText(string);
    ///seteaza textul cu stringul dat de utilizator

    Message& operator = (const Message&);
    ///operatorul de atribuire

    bool operator == (const Message&);
    ///opreatorul de egalitate

    ~Message();
    ///destructorul
};