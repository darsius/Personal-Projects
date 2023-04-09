
#include "Message.h"

Message::Message() {
    this->name1 = "";
    this->name2 = "";
    this->text = "";
}

Message::Message(string name1, string name2, string text) {
    this->name1 = name1;
    this->name2 = name2;
    this->text = text;
}

Message::Message(const Message &m) {
    this->name1 = m.name1;
    this->name2 = m.name2;
    this->text = m.text;
}

string Message::getName1() {
    return this->name1;
}

string Message::getName2() {
    return this->name2;
}

string Message::getText() {
    return this->text;
}

void Message::setName1(string name1) {
    this->name1 = name1;
}

void Message::setName2(string name2) {
    this->name2 = name2;
}

void Message::setText(string text) {
    this->text = text;
}

Message &Message::operator=(const Message &m) {
    this->name1 = m.name1;
    this->name2 = m.name2;
    this->text = m.text;
}

bool Message::operator==(const Message &m) {
    return this->name1 == m.name1 && this->name2 == m.name2 && this->text == m.text;
}

Message::~Message() {

}
