package socialnetwork.service;

import socialnetwork.domain.FriendRequest;
import socialnetwork.domain.Friendship;
import socialnetwork.domain.User;
import socialnetwork.repository.FriendRequestRepository;
import socialnetwork.repository.FriendshipRepository;
import socialnetwork.repository.UserRepository;
import socialnetwork.utils.events.Event;
import socialnetwork.utils.observer.Observable;
import socialnetwork.utils.observer.Observer;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.*;

public class Service implements Observable<Event> {
    private Connection connection;
    private UserRepository userRepository;
    private FriendshipRepository friendshipRepository;
    private FriendRequestRepository friendRequestRepository;
    private List<Observer<Event>> observers;

    Comparator<User> stringComparator = new Comparator<User>() {
        @Override
        public int compare(User user1, User user2) {
            return user1.getUsername().compareTo(user2.getUsername());
        }
    };
    Comparator<FriendRequest> dateComparator = new Comparator<FriendRequest>() {
        @Override
        public int compare(FriendRequest friendRequest1, FriendRequest friendRequest2) {
            return friendRequest1.getDate().compareTo(friendRequest2.getDate());
        }
    };



    public Service(UserRepository userRepository,
                   FriendshipRepository friendshipRepository,
                   FriendRequestRepository friendRequestRepository){
        this.userRepository = userRepository;
        this.friendshipRepository = friendshipRepository;
        this.friendRequestRepository = friendRequestRepository;
        observers = new ArrayList<>();
        try{
            connection = DriverManager.getConnection("jdbc:postgresql://localhost:5432/socialnetwork5", "postgres", "6162");
        }catch (SQLException e) {
            e.printStackTrace();
        }
    }

    //user
    public User addUser(User user) {
        return userRepository.save(user);
    }

    public User deleteUser(Long userId) {
        return userRepository.delete(userId);
    }

    public User updateUser(User user) {
        return userRepository.update(user);
    }

    public User findOneUser(Long userId) {
        return userRepository.findOne(userId);
    }
    public User findOneUserByUsername(String username) {
        return userRepository.findOneByUsername(username);
    }

    public ArrayList<User> findAllUsers(){
        return userRepository.findAll();
    }

    public List<User> findAllExceptYou(Long id){
        return userRepository.findAllExceptYou(id);
    }

    public List<User> getFriends(Long id) {
        List<Friendship> friendships = friendshipRepository.findFriendships(id);
        List<User> friends = new ArrayList<>();

        for (int i = 0; i < friendships.size(); i++){
            if (Objects.equals(friendships.get(i).getUtilizator1(), id))
                friends.add(userRepository.findOne(friendships.get(i).getUtilizator2()));
            else
                friends.add(userRepository.findOne(friendships.get(i).getUtilizator1()));
        }
//        for (int i = 0; i< friends.size(); i++){
//            System.out.println(friends.get(i).getUsername());
//        }

        // sort the list using the comparator
        Collections.sort(friends, stringComparator);

        return friends;
    }

    public Long getIdUserByUsername(String username){
        return userRepository.getIdUserByUsername(username);
    }

    //friendship

    public Friendship addFriendship(Friendship friendship){
        return friendshipRepository.save(friendship);
    }

    public Friendship deleteFriendship(Long idFriendship) {
        return friendshipRepository.delete(idFriendship);
    }

    public Friendship updateFriendship(Friendship friendship){
        return friendshipRepository.update(friendship);
    }

    public Friendship findOneFriendship(Friendship friendship) {
        return friendshipRepository.update(friendship);
    }

    public Iterable<Friendship> findAllFriendships() {
        return friendshipRepository.findAll();
    }

    public List<Friendship> getFriendships(Long id){
        return friendshipRepository.findFriendships(id);
    }

    //friendRequest
    public FriendRequest addFriendRequest(FriendRequest friendRequest) {
        return friendRequestRepository.save(friendRequest);

    }

    public FriendRequest deleteFriendRequest(Long idFriendRequest) {
        return friendRequestRepository.delete(idFriendRequest);
    }

    public FriendRequest updateFriendRequest(FriendRequest friendRequest) {
        return friendRequestRepository.update(friendRequest);
    }

    public FriendRequest findOneFriendRequest(Long idFriendRequest) {
        return friendRequestRepository.findOne(idFriendRequest);
    }

    public Iterable<FriendRequest> findAllFriendRequests(){
        return friendRequestRepository.findAll();
    }

    public List<FriendRequest> getFriendRequests(Long userId){
        Collections.sort(friendRequestRepository.findFriendRequests(userId), dateComparator);

        return friendRequestRepository.findFriendRequests(userId);
    }

    public Integer getFriendRequestsNumber(Long userId){
        return friendRequestRepository.findFriendRequests(userId).size();
    }
    @Override
    public void addObserver(Observer<Event> e) {
        observers.add(e);
    }

    @Override
    public void removeObserver(Observer<Event> e) {
        observers.remove(e);
    }

    @Override
    public void notifyObservers(Event t) {
        observers.forEach(o -> o.update(t));
    }

//    public List<User> searchUser(String searchText, Long id) {
//        return userRepository.findAllExceptYou(id)
//                .stream()
//                .filter(user -> user.getUsername().startsWith(searchText))
//                .collect(Collectors.toList());
//    }
}
