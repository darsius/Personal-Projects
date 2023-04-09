//

#include <cstring>
#include "User.h"

User::User() {
    this->id = 0;
    this->name = "";
}

User::User(int id, string name) {
    this->id = id;
    this->name = name;
}

User::User(const User &u) {
    this->id = u.id;
    this->name = u.name;
}

string User::getName() {
    return this->name;
}

int User::getId() {
    return this->id;
}

void User::setName(string name) {
    this->name = name;
}

void User::setId(int id) {
    this->id = id;
}

bool User::operator==(const User &u) {
    return this->id == u.id;
}

bool User::operator!=(const User &u) {
    return this->id != u.id ;
}

User &User::operator=(const User &u) {
    this->id = u.id;
    this->name = u.name;
    return *this;
}

bool User::operator>(const User &u) {
    return id > u.id;
}

bool User::operator<(const User &u) {
    return this->id < u.id;
}

istream &operator>>(istream &is, User &u) {
    is >> u.id >> u.name ;
    return is;
}

ostream &operator<<(ostream &os, User &u) {
    os << u.id << " " << u.name ;
    return os;
}

User::~User() {
    this->id = 0;
    this->name = "";
}
