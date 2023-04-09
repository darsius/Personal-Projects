//
// Created by p_dar on 5/16/2022.
//

#include "Friendship.h"

Friendship::Friendship() {
    this->name1 = "";
    this->name2 = "";
}

Friendship::Friendship(string nume1, string nume2) {
    this->name1 = nume1;
    this->name2 = nume2;
}

Friendship::Friendship(const Friendship &f) {
    this->name1 = f.name1;
    this->name2 = f.name2;
}



void Friendship::setName1(string nume1) {
    this->name1 = nume1;
}

void Friendship::setName2(string nume2) {
    this->name2 = nume2;
}

Friendship &Friendship::operator=(const Friendship &f) {
    this->name1 = f.name1;
    this->name2 = f.name2;
}

bool Friendship::operator==(const Friendship &f) {
    return this->name1 == f.name1 && this->name2 == f.name2;
}

bool Friendship::operator!=(const Friendship &f) {
    return this->name2 != f.name2 || this->name1 != f.name1;
}

Friendship::~Friendship() {

}

string Friendship::getName1() {
    return this->name1;
}

string Friendship::getName2() {
    return this->name2;
}
