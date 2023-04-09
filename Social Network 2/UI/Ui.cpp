//
// Created by p_dar on 4/30/2022.
//

#include "Ui.h"
#include <iostream>
using namespace std;


void Ui::showMenu() {
    int opt = 99;

    while (opt != 0){
        cout << "1. Gestionare utilizatori: " << endl;
        cout << "2. Gestionare prieteni: " << endl;
        cout << "3. Gestionare mesaje: " << endl;
        cout << "4. Iesire" << endl;

        cout << "Dati optiunea: " << endl;
        cin >> opt;
        switch (opt) {
            case 1: {menuUser(); break;}
            case 2: {menuFriendship(); break;}
            case 3: {menuMessage(); break;}
            case 4: return;
            default: cout << "Optiune invalida! Reincercati " << endl;
        }
    }
}



Ui::Ui() {
    this->serviceUser = serviceUser;
    this->serviceFriendship = serviceFriendship;
    this->serviceMessage = serviceMessage;
}

void Ui::addUser() {
    int id;
    string name;
    cout << "Dati id-ul utilizatorului de adaugat: "<< endl;
    cin >> id;
    cout << "Dati numele utilizatorului de adaugat: "<< endl;
    cin >> name;

    this->serviceUser.addUser(id, name);
}

void Ui::removeUser() {
    int id ;
    string name;
    cout << "Dati id-ul utilizatorului de sters: " << endl;
    cin >> id;
    cout << "Dati numele utilizatorului de sters: "<< endl;
    cin >> name;

    this->serviceUser.removeUser(id, name);
}

void Ui::updateUser() {
    int id;
    string name;
    cout << "Dati id-ul utilizatorului de actualizat: "<< endl;
    cin >> id;
    cout << "Dati numele utilizatorului de actualizat: "<< endl;
    cin >> name;

    int newId;
    string newName;
    cout << "Dati id-ul noului utilizator: "<< endl;
    cin >> newId;
    cout << "Dati numele noului utilizator: "<< endl;
    cin >> newName;

    this->serviceUser.updateUser(id, name, newId, newName);
}

void Ui::searchUser() {

}

Ui::Ui(ServiceUser &serviceUser, ServiceFriendship &serviceFriendship, ServiceMessage &serviceMessage) {

}

void Ui::showAllUsers() {
    serviceUser.showAll();
//    vector<User> rez = serviceUser.getAll();
//    for (int i = 0; i< rez.size(); i++){
//        cout << rez[i].getId() << " " << rez[i].getNume() << endl;
//    }
}

void Ui::menuUser() {
    int opt = 99;

    while (opt != 0) {
        cout << "1. Adaugare utlizator. " << endl;
        cout << "2. Stergere utlizator. " << endl;
        cout << "3. Actualizare utilizator. " << endl;
        cout << "4. Afisare toti. " << endl;
        cout << "5. Intoarcere meniu principal. " << endl;
        cout << "Dati optiunea: " << endl;
        cin >> opt;
        switch (opt) {
            case 1: {addUser();break;}
            case 2: {removeUser();break;}
            case 3: {updateUser(); break;}
            case 4: {showAllUsers(); break;}
            case 5: {showMenu(); break;}
            default: cout << "Optiune invalida! Reincercati " << endl;
        }
    }
}

void Ui::menuFriendship() {
    int opt = 99;

    while (opt != 0) {
        cout << "1. Adaugare prieten. " << endl;
        cout << "2. Stergere prieten. " << endl;
        cout << "3. Afisare prieteni. " << endl;
        cout << "4. Afisare prieteni pentru un user. " << endl;
        cout << "5. Intoarcere meniu principal. " << endl;
        cout << "Dati optiunea: " << endl;
        cin >> opt;
        switch (opt) {
            case 1: {addFriend();break;}
            case 2: {removeFriend();break;}
            case 3: {showAllFriends(); break;}
            case 4: {showFriendsForAnUser(); break;}
            case 5: {showMenu(); break;}
            default: cout << "Optiune invalida! Reincercati " << endl;
        }
    }
}

void Ui::menuMessage() {
    int opt = 99;

    while (opt != 0) {
        cout << "1. Adaugare mesaj. " << endl;
        cout << "2. Stergere mesaj. " << endl;
        cout << "3. Afisare mesaje pentru un user. " << endl;
        cout << "4. Afisare toate mesajele. " << endl;
        cout << "5. Intoarcere meniu principal. " << endl;
        cout << "Dati optiunea: " << endl;
        cin >> opt;
        switch (opt) {
            case 1: {addMessage();break;}
            case 2: {removeMessage();break;}
            case 3: {showAllMessagesForAnUser(); break;}
            case 4: {showAllMessages(); break;}
            case 5: {showMenu(); break;}
            default: cout << "Optiune invalida! Reincercati " << endl;
        }
    }
}

void Ui::addMessage() {
    string name1;
    string name2;
    string text;
    cout << "Dati numele utilizatorului care trimite mesajul: "<< endl;
    cin >> name1;
    cout << "Dati numele utilizatorului care primeste mesajul: "<< endl;
    cin >> name2;
    cout << "Dati mesajul: "<< endl;
    cin.ignore();
    getline(cin, text);
    this->serviceMessage.addMessage(name1, name2,  text);
}

void Ui::removeMessage() {
    string name1;
    string name2;
    string text;
    cout << "Dati numele utilizatorului care trimite mesajul: "<< endl;
    cin >> name1;
    cout << "Dati numele utilizatorului care primeste mesajul: "<< endl;
    cin >> name2;
    cout << "Dati mesajul de sters: "<< endl;
    cin.ignore();
    getline(cin, text);
    this->serviceMessage.removeMessage(name1, name2,  text);
}

void Ui::showAllMessages() {
    Message* rez = serviceMessage.getAll();
    for (int i = 0; i< serviceMessage.getSize(); i++){
        cout << rez[i].getName1() << " -- " << rez[i].getName2() << endl;
        cout << rez[i].getText() << endl;
        cout << endl;
    }
}

void Ui::addFriend() {
    string name1;
    string name2;
    cout << "Dati numele utilizatorului care trimite cererea de prietenie: "<< endl;
    cin >> name1;
    cout << "Dati numele utilizatorului care primeste cererea de prietenie: "<< endl;
    cin >> name2;
    serviceFriendship.addFriendship(name1, name2);
}

void Ui::removeFriend() {
    string name1;
    string name2;
    cout << "Dati numele primului utilizator: "<< endl;
    cin >> name1;
    cout << "Dati numele celui de-al doilea utilizator: "<< endl;
    cin >> name2;
    serviceFriendship.removeFriendship(name1, name2);
}

void Ui::showAllFriends() {
    Set<string> m;
    Friendship *rez = this->serviceFriendship.getAll();
    for (int i = 0; i < this->serviceFriendship.getSize(); i++){
        if(!m.search(rez[i].getName1()))
            m.add(rez[i].getName1());
        if(!m.search(rez[i].getName2()))
            m.add(rez[i].getName2());
    }
    vector<string> p = m.getAll();
    for (int i = 0; i < p.size(); i++){
        cout << p[i] <<": ";
        vector<string> rez = serviceFriendship.showFriendsForAnUser(p[i]);
        if (rez.size() != 0){
            for ( int i = 0; i < rez.size(); i++)
            if ( i == 0)
                cout << rez[i];
            else
                cout <<"," << rez[i];
        }
        cout << endl;
    }
}

void Ui::showFriendsForAnUser() {
    string name;
    cout << "Dati numele userului caruia vreti sa ii vedeti prietenii: " << endl;
    cin >> name;
    cout << name << ": ";
    vector<string> rez = serviceFriendship.showFriendsForAnUser(name);
    for ( int i = 0; i < rez.size(); i++)
        if ( i == 0)
            cout << rez[i];
        else
            cout <<"," << rez[i];
    cout << endl;

}

void Ui::showAllMessagesForAnUser() {
    string name;
    cout << "Dati numele userului caruia vreti sa ii vedeti mesajele: " << endl;
    cin >> name;
    vector<string> rez = serviceMessage.showMessagesForAnUser(name);
    Message* lst = serviceMessage.getAll();
    Set<string> friends;
    for(int i = 0; i<serviceMessage.getSize(); i++){
        friends.add(lst[i].getName1());
        friends.add(lst[i].getName2());
    }
    for ( int i = 0; i < rez.size()-1; i+=2){
        cout <<name<<" <--> "<<rez[i]<<endl;
        cout <<"Mesaje: "<<rez[i+1]<<endl;
    }
}

void Ui::addEntityes() {
    serviceUser.addUser(1, "Ana");
    serviceUser.addUser(2, "Bea");
    serviceUser.addUser(3, "Paul");
    serviceUser.addUser(4, "Geo");
    serviceUser.addUser(5, "Ari");
    serviceUser.addUser(6, "Iri");
    serviceUser.addUser(7, "Elena");
    serviceUser.addUser(8, "Maria");
    serviceUser.addUser(9, "Darius");
    serviceUser.addUser(10, "Edu");
    serviceUser.addUser(11, "Lea");
    serviceUser.addUser(12, "Paula");
    serviceUser.addUser(13, "Eli");
    serviceUser.addUser(14, "Leo");
    serviceUser.addUser(15, "Denis");

    serviceFriendship.addFriendship("Ana", "Bea");
    serviceFriendship.addFriendship("Ana", "Paul");
    serviceFriendship.addFriendship("Bea", "Paul");
    serviceFriendship.addFriendship("Geo", "Ari");
    serviceFriendship.addFriendship("Iri", "Geo");
    serviceFriendship.addFriendship("Iri", "Ari");
    serviceFriendship.addFriendship("Elena", "Bea");
    serviceFriendship.addFriendship("Maria", "Elena");
    serviceFriendship.addFriendship("Eli", "Maria");
    serviceFriendship.addFriendship("Darius", "Maria");
    serviceFriendship.addFriendship("Elena", "Darius");
    serviceFriendship.addFriendship("Darius", "Edu");
    serviceFriendship.addFriendship("Edu", "Lea");
    serviceFriendship.addFriendship("Lea", "Leo");
    serviceFriendship.addFriendship("Ana", "Leo");
    serviceFriendship.addFriendship("Denis", "Elena");
    serviceFriendship.addFriendship("Eli", "Paula");
    serviceFriendship.addFriendship("Ana", "Iri");

    serviceMessage.addMessage("Ana", "Bea", "Hai afara!");
    serviceMessage.addMessage("Bea", "Paul", "Da.");
    serviceMessage.addMessage("Geo", "Ari", "Vin imediat.");
    serviceMessage.addMessage("Iri", "Geo", "Iesim azi?");
    serviceMessage.addMessage("Maria", "Elena", "Nu credd!");
    serviceMessage.addMessage("Ana", "Bea", "Kebab sau pizza");
    serviceMessage.addMessage("Bea", "Paul", "N-am stiut");
    serviceMessage.addMessage("Darius", "Maria", "Ai tema?");
    serviceMessage.addMessage("Edu", "Lea", "Mergem sa vedem scena.");
    serviceMessage.addMessage("Lea", "Leo", "Nu");
    serviceMessage.addMessage("Ana", "Bea", "Cum se numea melodia?");
    serviceMessage.addMessage("Bea", "Paul", "A zis ca da.");
    serviceMessage.addMessage("Denis", "Elena", "Poate.");
    serviceMessage.addMessage("Eli", "Paula", "In fata la faculta.");
    serviceMessage.addMessage("Paula", "Bea", "Luni ajunge.");

}

Ui::~Ui() = default;
