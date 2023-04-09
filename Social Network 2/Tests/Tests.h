#include <iostream>
#include <cassert>
#include "../Domain/User.h"
#include "../Domain/User.cpp"
#include "../UI/Ui.h"
#include <cstring>
#include "vector"

using namespace std;


void UserTests(){
    User u1(1, "Paul");
    User u2(2, "Andreea");
    User u3(3, "Geo");
    User u4(4, "Ana");
    User u5(5, "Iri");

    assert(u1.getId() == 1);
    assert(u1.getName() == "Paul");

    assert(u2.getId() == 2);
    assert(u2.getName() == "Andreea");

    assert(u3.getId() == 3);
    assert(u3.getName() == "Geo");

    assert(u4.getId() == 4);
    assert(u4.getName() == "Ana");

    assert(u5.getId() == 5);
    assert(u5.getName() == "Iri");
}

void MessageTests(){
    Message m1("Ana", "Geo", "Vii?");
    Message m2("Paul", "Geo", "Adu mingea la teren.");
    Message m3("Roxi", "Rea", "Bea apa.");
    Message m4("Nini", "Eli", "Ai tema?");
    Message m5("Bogdan", "Lea", "Nu.");

    assert(m1.getName1() == "Ana");
    assert(m1.getName2() == "Geo");
    assert(m1.getText() == "Vii?");

    assert(m2.getName1() == "Paul");
    assert(m2.getName2() == "Geo");
    assert(m2.getText() == "Adu mingea la teren.");

    assert(m3.getName1() == "Roxi");
    assert(m3.getName2() == "Rea");
    assert(m3.getText() == "Bea apa.");

    assert(m4.getName1() == "Nini");
    assert(m4.getName2() == "Eli");
    assert(m4.getText() == "Ai tema?");

    assert(m5.getName1() == "Bogdan");
    assert(m5.getName2() == "Lea");
    assert(m5.getText() == "Nu.");
}

void FriendshipTests(){
    Friendship f1("Ana", "Geo");
    Friendship f2("Paul", "Geo");
    Friendship f3("Roxi", "Rea");
    Friendship f4("Nini", "Eli");
    Friendship f5("Bogdan", "Lea");

    assert(f1.getName1() == "Ana");
    assert(f2.getName1() == "Paul");
    assert(f3.getName1() == "Roxi");
    assert(f4.getName1() == "Nini");
    assert(f5.getName1() == "Bogdan");

    assert(f1.getName2() == "Geo");
    assert(f2.getName2() == "Geo");
    assert(f3.getName2() == "Rea");
    assert(f4.getName2() == "Eli");
    assert(f5.getName2() == "Lea");
}


void ListTests(){
    List<Friendship> list;
    Friendship f1("Ana", "Geo");
    Friendship f2("Paul", "Geo");
    Friendship f3("Roxi", "Rea");
    Friendship f4("Nini", "Eli");
    Friendship f5("Bogdan", "Lea");
    Friendship f6("Ale", "Dea");

    list.add(f1);
    list.add(f2);
    list.add(f3);
    list.add(f4);
    list.add(f5);
//    assert(list.length() == 5);

//    list.remove(f5);
//    assert(list.length() == 4);
//
//    list.update(f1, f6);
//    assert(list[0].getName1() == "Ale");
//    assert(list[0].getName2() == "Dea");
}

void TreeTests(){
    Tree<User> tree;
    User u1(1, "Paul");
    User u2(2, "Andreea");
    User u3(3, "Geo");
    User u4(4, "Ana");
    User u5(5, "Iri");

    tree.add(u1);
    tree.add(u2);
    tree.add(u3);
    tree.add(u4);
    tree.add(u5);
    vector<User> v = tree.getAll();
    assert(v[0].getId() == 1);
    assert(v[0].getName() == "Paul");
    assert(v[4].getId() == 5);
    assert(v[4].getName() == "Iri");
}

void SeTests(){
    Set<User> set;
    User u1(1, "Paul");
    User u2(2, "Andreea");
    User u3(3, "Geo");
    User u4(4, "Ana");
    User u5(5, "Iri");

    set.add(u1);
    set.add(u2);
    set.add(u3);
    set.add(u4);
    set.add(u5);

    set.add(u5);
    vector<User> v = set.getAll();
    assert(v[0].getId() == 1);
    assert(v[0].getName() == "Paul");
    assert(v[4].getId() == 5);
    assert(v[4].getName() == "Iri");
    assert(v[3].getId() != 5);
    assert(v[3].getName() != "Iri");
    assert(v[5].getId() != 5);
    assert(v[5].getName() != "Iri");
}

void RepositoryFriendshipTests(){
    RepositoryFriendship<Friendship> r;
    Friendship f1("Ana", "Geo");
    Friendship f2("Paul", "Geo");
    Friendship f3("Roxi", "Rea");
    Friendship f4("Nini", "Eli");
    Friendship f5("Bogdan", "Lea");

    r.add(f1);
    r.add(f2);
    r.add(f3);
    r.add(f4);
    r.add(f5);
    assert(r.size() == 5);

    r.remove(f1);
    r.remove(f2);
    assert(r.size() == 3);
}

void RepositoryMessagesTests(){
    RepositoryMessage<Message> r;
    Message m1("Ana", "Geo", "Vii?");
    Message m2("Paul", "Geo", "Adu mingea la teren.");
    Message m3("Roxi", "Rea", "Bea apa.");
    Message m4("Nini", "Eli", "Ai tema?");
    Message m5("Bogdan", "Lea", "Nu.");

    r.add(m1);
    r.add(m2);
    r.add(m3);
    r.add(m4);
    r.add(m5);
    assert(r.size() == 5);

    r.remove(m3);
    assert(r.size() == 4);
}

void RepositoryUserTests(){
    RepositoryUser<User> r;
    User u1(1, "Paul");
    User u2(2, "Andreea");
    User u3(3, "Geo");
    User u4(4, "Ana");
    User u5(5, "Iri");

    r.add(u1);
    r.add(u2);
    r.add(u3);
    r.add(u4);
    r.add(u5);

    vector<User> v = r.getAll();

    assert(v[0].getId() == 1);
    assert(v[1].getId() == 2);
    assert(v[2].getId() == 3);
    assert(v[3].getId() == 4);
    assert(v[4].getId() == 5);

    assert(v[0].getName() == "Paul");
    assert(v[1].getName() == "Andreea");
    assert(v[2].getName() == "Geo");
    assert(v[3].getName() == "Ana");
    assert(v[4].getName() == "Iri");
}

void ServiceFriendshpTests(){
    ServiceFriendship s;
    s.addFriendship("Ana", "Geo");
    s.addFriendship("Paul", "Geo");
    s.addFriendship("Roxi", "Rea");
    s.addFriendship("Nini", "Eli");
    s.addFriendship("Bogdan", "Lea");
    assert(s.getSize() == 5);

    s.removeFriendship("Ana", "Geo");
    assert(s.getSize() == 4);
}

void ServiceMessagesTests(){
    ServiceMessage s;
    s.addMessage("Ana", "Geo", "Nu.");
    s.addMessage("Paul", "Geo", "Stam inca o ora.");
    s.addMessage("Roxi", "Rea", "Pai?");
    s.addMessage("Nini", "Eli", "Da.");
    s.addMessage("Bogdan", "Lea", "GG.");
    assert(s.getSize() == 5);

    s.removeMessage("Bogdan", "Lea", "GG.");
    assert(s.getSize() == 4);
}

void ServiceUserTests(){
    ServiceUser s;
    s.addUser(1, "Ana");
    s.addUser(2, "Roxi");
    s.addUser(3, "Iri");
    s.addUser(4, "Geo");
    s.addUser(5, "Lea");

    vector<User> v = s.getAll();
    assert(v.size() == 5);
}

void domainTests(){
    UserTests();
    MessageTests();
    FriendshipTests();
    ListTests();
    TreeTests();
    SeTests();
}

void repositoryTests(){
    RepositoryFriendshipTests();
    RepositoryMessagesTests();
    RepositoryUserTests();
}

void serviceTests(){
    ServiceFriendshpTests();
    ServiceMessagesTests();
    ServiceUserTests();
}


void runAllTests(){
    domainTests();
//    repositoryTests();
//    serviceTests();
}
