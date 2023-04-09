package socialnetwork.repository;

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
import java.util.List;

public class FriendshipRepository implements Repository<Long, Friendship>, Observable<Event> {
    private Connection connection;
    private Validator<Friendship> validator;
    private List<Observer<Event>> observers;

    public FriendshipRepository(Connection connection, Validator<Friendship> validator){
        this.connection = connection;
        this.validator = validator;
        this.observers = new ArrayList<>();
    }
    @Override
    public Friendship findOne(Long id) {
        Friendship friendship = null;
        try {
            PreparedStatement preparedStatement = connection.prepareStatement("SELECT * FROM friendship WHERE id_user1=? OR id_user2 =?");
            preparedStatement.setLong(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                friendship = new Friendship();
                friendship.setId(resultSet.getLong("id"));
                friendship.setUtilizator1(resultSet.getLong("id_user1"));
                friendship.setUtilizator1(resultSet.getLong("id_user2"));
                friendship.setDate(resultSet.getDate("date"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return friendship;
    }

    @Override
    public Iterable<Friendship> findAll() {
        List<Friendship> friendships = new ArrayList<>();
        try{
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery("SELECT * FROM friendships");
            while (resultSet.next()){
                Friendship friendship = new Friendship();
                friendship.setId(resultSet.getLong("id"));
                friendship.setUtilizator1(resultSet.getLong("id_user1"));
                friendship.setUtilizator1(resultSet.getLong("id_user2"));
                friendship.setDate(resultSet.getDate("date"));
                friendships.add(friendship);
            }
        }catch (SQLException e) {
            e.printStackTrace();
        }
        return friendships;
    }

    @Override
    public Friendship save(Friendship entity) {
        System.out.println("A");
        Friendship friendship = entity;
        try {
            System.out.println('B');
            PreparedStatement preparedStatement = connection.prepareStatement("Insert into friendship(id_user1, id_user2, date) values (?, ?, ?)");
            preparedStatement.setLong(1, friendship.getUtilizator1());
            preparedStatement.setLong(2, friendship.getUtilizator2());
            preparedStatement.setDate(3, friendship.getDate());
            System.out.println('C');
            preparedStatement.executeUpdate();
            System.out.println('D');
            notifyObservers(new ChangeEvent(ChangeEventType.ADD, friendship));
            System.out.println("MERGEE");
        }catch (SQLException e) {
            e.printStackTrace();
        }
        return friendship;
    }

    @Override
    public Friendship delete(Long id) {
        Friendship friendship = findOne(id);
        if (friendship != null) {
            try {
                PreparedStatement preparedStatement = connection.prepareStatement("DELETE FROM friendship WHERE id = ?");
                preparedStatement.setLong(1, id);
                preparedStatement.executeUpdate();
                notifyObservers(new ChangeEvent(ChangeEventType.DELETE, friendship));
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        return friendship;
    }


    @Override
    public Friendship update(Friendship friendship) {
        try{
            PreparedStatement preparedStatement = connection.prepareStatement("UPDATE friendship SET id_user1=?, id_user2=?, date=? WHERE id_user2=?");
            preparedStatement.setLong(1, friendship.getUtilizator1());
            preparedStatement.setLong(2, friendship.getUtilizator2());
            preparedStatement.setDate(3, friendship.getDate());
            preparedStatement.setLong(4, friendship.getId());
            preparedStatement.executeUpdate();
            notifyObservers(new ChangeEvent(ChangeEventType.UPDATE, friendship));
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return friendship;
    }

    //
    public List<Friendship> findFriendships(Long id_user1){
        List<Friendship> friendships = new ArrayList<>();
        try{
            PreparedStatement preparedStatement = connection.prepareStatement("select * from friendship where id_user1 = ? or id_user2 = ?");
            preparedStatement.setLong(1, id_user1);
            preparedStatement.setLong(2, id_user1);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()){
                Friendship friendship = new Friendship();
                friendship.setUtilizator1(resultSet.getLong("id_user1"));
                friendship.setUtilizator2(resultSet.getLong("id_user2"));
                friendship.setDate(resultSet.getDate("date"));
                friendships.add(friendship);
            }
        }catch (SQLException e) {
            e.printStackTrace();
        }
        return friendships;
    }



    //

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
