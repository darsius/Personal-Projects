package socialnetwork.repository;

import socialnetwork.domain.FriendRequest;
import socialnetwork.domain.Friendship;
import socialnetwork.domain.validators.Validator;
import socialnetwork.repository.Repository;
import socialnetwork.utils.events.ChangeEvent;
import socialnetwork.utils.events.ChangeEventType;
import socialnetwork.utils.events.Event;
import socialnetwork.utils.observer.Observable;
import socialnetwork.utils.observer.Observer;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class FriendRequestRepository implements Repository<Long, FriendRequest>, Observable<Event> {

    private Connection connection;
    private Validator<FriendRequest> validator;
    private List<Observer<Event>> observers;

    public FriendRequestRepository(Connection connection, Validator<FriendRequest> validator){
        this.connection = connection;
        this.validator = validator;
        this.observers = new ArrayList<>();
    }
    @Override
    public FriendRequest findOne(Long id) {
        try{
            String sql = "SELECT * FROM friend_request WHERE id_receiver = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setLong(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                FriendRequest friendRequest = new FriendRequest();
                friendRequest.setId(resultSet.getLong("id"));
                friendRequest.setReceiverId(resultSet.getLong("id_receiver"));
                friendRequest.setReceiverId(resultSet.getLong("id_sender"));
                friendRequest.setDate(resultSet.getDate("date"));
                return friendRequest;
            }

        }catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }
//    public Iterable<Utilizator> findAll() {
//        Set<Utilizator> users = new HashSet<>();
//        try (Connection connection = DriverManager.getConnection(url, username, password);
//             PreparedStatement statement = connection.prepareStatement("SELECT * from users");
//             ResultSet resultSet = statement.executeQuery()) {
//
//            while (resultSet.next()) {
//                Long id = resultSet.getLong("id");
//                String firstName = resultSet.getString("first_name");
//                String lastName = resultSet.getString("last_name");
//                String username = this.username;
//
//                Utilizator utilizator = new Utilizator(firstName, lastName, username);
//                utilizator.setId(id);
//                users.add(utilizator);
//            }
//            return users;
//        } catch (SQLException e) {
//            e.printStackTrace();
//        }
//        return users;
//    }

    @Override
    public Iterable<FriendRequest> findAll() {
        try {
            String sql = "SELECT * FROM friend_request";
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(sql);
            List<FriendRequest> friendRequests = new ArrayList<>();
            while (resultSet.next()) {
                FriendRequest friendRequest = new FriendRequest();
                friendRequest.setId(resultSet.getLong("id"));
                friendRequest.setReceiverId(resultSet.getLong("id_receiver"));
                friendRequest.setSenderId(resultSet.getLong("id_sender"));
                friendRequest.setDate(resultSet.getDate("date"));
                friendRequests.add(friendRequest);
            }
            return friendRequests;
        }catch (SQLException e) {
            e.printStackTrace();
        }
        return null;
    }

    @Override
    public FriendRequest save(FriendRequest entity) {
        FriendRequest friendRequest = entity;
        validator.validate(friendRequest);
        try {
            String sql = "INSERT INTO friend_request (id_sender, id_receiver, date) VALUES (?, ?, ?)";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setLong(1, friendRequest.getSenderId());
            preparedStatement.setLong(2, friendRequest.getReceiverId());
            preparedStatement.setDate(3, (Date) friendRequest.getDate());
            preparedStatement.executeUpdate();
            notifyObservers(new ChangeEvent(ChangeEventType.ADD,friendRequest));
        } catch (SQLException e) {
            e.getStackTrace();
        }

        return friendRequest;
    }

//    @Override
//    public FriendRequest delete(Long id) {
//        FriendRequest friendRequest = findOne(id);
//        try{
//            String sql = "DELETE FROM friend_request WHERE id = ?";
//            PreparedStatement preparedStatement = connection.prepareStatement(sql);
//            preparedStatement.setLong(1, id);
//            preparedStatement.executeUpdate();
//            notifyObservers(new ChangeEvent(ChangeEventType.DELETE, friendRequest));
//
//        }catch (SQLException e) {
//            e.printStackTrace();
//        }
//        return friendRequest;
//    }
    @Override
    public FriendRequest delete(Long id) {
        FriendRequest friendRequest = findOne(id);
        try{
            String sql = "DELETE FROM friend_request WHERE id_receiver = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setLong(1, id);
            preparedStatement.executeUpdate();
            notifyObservers(new ChangeEvent(ChangeEventType.DELETE, friendRequest));

        }catch (SQLException e) {
            e.printStackTrace();
        }
        return friendRequest;
    }

    @Override
    public FriendRequest update(FriendRequest entity) {
        FriendRequest friendRequest = entity;
        validator.validate(friendRequest);
        try{
            String sql = "UPDATE friend_request SET id_sender = ?, id_receiver = ?, date = ? WHERE id_receiver = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setLong(1, friendRequest.getReceiverId());
            preparedStatement.setLong(2, friendRequest.getSenderId());
            preparedStatement.setDate(3, (Date) friendRequest.getDate());
            preparedStatement.setLong(4, friendRequest.getId());
            preparedStatement.executeUpdate();
            notifyObservers(new ChangeEvent(ChangeEventType.UPDATE, friendRequest));
            return entity;
        }catch (SQLException e) {
            e.printStackTrace();
        }
        return entity;
    }

    public List<FriendRequest> findFriendRequests(Long id_user){
        List<FriendRequest> friendRequests = new ArrayList<>();
        try{
            PreparedStatement preparedStatement = connection.prepareStatement("select * from friend_request where id_receiver = ?");
            preparedStatement.setLong(1, id_user);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()){
                FriendRequest friendRequest = new FriendRequest();
                friendRequest.setSenderId(resultSet.getLong("id_sender"));
                friendRequest.setReceiverId(resultSet.getLong("id_receiver"));
                friendRequest.setDate(resultSet.getDate("date"));
                friendRequests.add(friendRequest);
            }

        }catch (SQLException e) {
            e.printStackTrace();
        }
        return friendRequests;
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
}
