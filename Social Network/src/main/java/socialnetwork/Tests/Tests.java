package socialnetwork.Tests;

import socialnetwork.domain.FriendRequest;
import socialnetwork.domain.Friendship;
import socialnetwork.domain.User;
import socialnetwork.domain.validators.FriendRequestValidator;
import socialnetwork.domain.validators.FriendshipValidator;
import socialnetwork.domain.validators.UserValidator;
import socialnetwork.repository.FriendRequestRepository;
import socialnetwork.repository.FriendshipRepository;
import socialnetwork.repository.UserRepository;
import socialnetwork.service.Service;
import socialnetwork.utils.events.Event;
import socialnetwork.utils.observer.Observer;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Vector;

public class Tests {
    User user1 = new User("a", "b", "c", "d");
    User user2 = new User("q", "r", "s", "t");

    Date date= new java.sql.Date(System.currentTimeMillis());

    Friendship friendship1 = new Friendship(user1.getId(), user2.getId(), (java.sql.Date) date);

    FriendRequest friendRequest1 = new FriendRequest(user1.getId(), user2.getId(), (java.sql.Date) date);
    private UserValidator userValidator;
    private FriendshipValidator friendshipValidator;
    private FriendRequestValidator friendRequestValidator;
    private List<Observer<Event>> observers;
    String username="postgres";
    String password="6162";
    String url="jdbc:postgresql://localhost:5432/socialnetwork5";

    Connection connection = DriverManager.getConnection(url, username, password);
    UserRepository userRepository = new UserRepository(connection, userValidator);
    FriendshipRepository friendshipRepository = new FriendshipRepository(connection, friendshipValidator);
    FriendRequestRepository friendRequestRepository = new FriendRequestRepository(connection, friendRequestValidator);

    public Tests() throws SQLException {
    }

    private void testUserRepository(){
//        userValidator.validate(user1);
//        userValidator.validate(user2);
//        userRepository.save(user1);
//        userRepository.save(user2);
        userRepository.delete(67L);
        ArrayList<User> users = userRepository.findAll();
        System.out.println(users.size());
//        assert users.get(0).equals(user1);
//        assert users.get(1).equals(user2);

//        User user3 = null;
//        user3 = userRepository.findOneByUsername(user1.getUsername());
//        assert user3.equals(user2);

//        users.remove(user1);
//        assert users.size() == 1;

    }
//
//    private void testFriendshipRepository(){
//        friendshipRepository.save(friendship1);
//
//    }
//
//    private void testFriendRequestRepository(){
//        friendRequestRepository.save(friendRequest1);
//    }
//
//    private void testService(){
//        Service service = new Service(userRepository, friendshipRepository, friendRequestRepository);
//
//    }

    public void testAll(){
        testUserRepository();
    }

}
