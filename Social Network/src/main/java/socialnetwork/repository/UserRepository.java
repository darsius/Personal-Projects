package socialnetwork.repository;

import socialnetwork.domain.User;
import socialnetwork.domain.validators.UserValidator;
import socialnetwork.repository.Repository;
import socialnetwork.utils.events.ChangeEvent;
import socialnetwork.utils.events.ChangeEventType;
import socialnetwork.utils.events.Event;
import socialnetwork.utils.observer.Observable;
import socialnetwork.utils.observer.Observer;

import java.sql.*;
import java.util.*;

public class UserRepository implements Repository<Long, User>, Observable<Event> {
    private Connection connection;
    private UserValidator validator;

    private List<Observer<Event>> observers;

    public UserRepository(Connection connection, UserValidator validator) {
        this.connection = connection;
        this.validator = validator;
        this.observers = new ArrayList<>();
    }
    @Override
    public User findOne(Long id) {
        User user = null;
        try {
            PreparedStatement preparedStatement = connection.prepareStatement("SELECT  * FROM users WHERE id =?");
            preparedStatement.setLong(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                user = new User();
                user.setId(resultSet.getLong("id"));
                user.setFirstName(resultSet.getString("first_name"));
                user.setLastName(resultSet.getString("last_name"));
                user.setUsername(resultSet.getString("username"));
                user.setPassword(resultSet.getString("password"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return user;
    }

    public User findOneByUsername(String username) {
        User user = null;
        try {
            PreparedStatement preparedStatement = connection.prepareStatement("SELECT  * FROM users WHERE username =?");
            preparedStatement.setString(1, username);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                user = new User();
                user.setId(resultSet.getLong("id"));
                user.setFirstName(resultSet.getString("first_name"));
                user.setLastName(resultSet.getString("last_name"));
                user.setUsername(resultSet.getString("username"));
                user.setPassword(resultSet.getString("password"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return user;
    }
    @Override
    public ArrayList<User> findAll() {
//        List<User> users = new HashSet<>();
        ArrayList<User> users = new ArrayList<>();
        try {
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery("SELECT * FROM  users");
            while (resultSet.next()) {
                User user = new User();
                user.setId(resultSet.getLong("id"));
                user.setFirstName(resultSet.getString("first_name"));
                user.setLastName(resultSet.getString("last_name"));
                user.setUsername(resultSet.getString("username"));
                user.setPassword(resultSet.getString("password"));
                users.add(user);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return users;
    }


    //TODO: findAllExceptYou()
    //public void createUser(Restultset rs, Statement st)
    @Override
    public User delete(Long id) {
        User user = findOne(id);
        if (user != null) {
            try{
                String sql = "delete from users where id = ?";
                PreparedStatement preparedStatement = connection.prepareStatement(sql);
                preparedStatement.setLong(1, id);
                preparedStatement.executeUpdate();
                notifyObservers(new ChangeEvent(ChangeEventType.DELETE, user));
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        return user;
    }

    @Override
    public User save(User entity) {
        User user = entity;
        validator.validate(user);
        try {
            String sql = "insert into users (first_name, last_name, username, password) values (?, ?, ?, ?)";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, user.getFirstName());
            preparedStatement.setString(2, user.getLastName());
            preparedStatement.setString(3, user.getUsername());
            preparedStatement.setString(4, user.getPassword());
            preparedStatement.executeUpdate();
            notifyObservers(new ChangeEvent(ChangeEventType.ADD, user));
            return user;
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return user;
    }

    @Override
    public User update(User entity) {
        User user = entity;
        validator.validate(user);
        try{
            String sql = "UPDATE users SET first_name = ?, last_name = ?, username = ?, password = ? WHERE id = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setString(1, user.getFirstName());
            preparedStatement.setString(2, user.getLastName());
            preparedStatement.setString(3, user.getUsername());
            preparedStatement.setString(4, user.getPassword());
            preparedStatement.setLong(5, user.getId());
            preparedStatement.executeUpdate();
            notifyObservers(new ChangeEvent(ChangeEventType.UPDATE, user));
            return user;
            //return entity;
        }catch (SQLException e) {
            e.printStackTrace();
        }
        return user;
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

    public List<User> findAllExceptYou(Long id) {
        List <User> users = new ArrayList<>();
        try{
            PreparedStatement preparedStatement = connection.prepareStatement("SELECT * FROM users WHERE NOT id = ?");
            preparedStatement.setLong(1, id);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()){
                User user = new User();
                user.setId(resultSet.getLong("id"));
                user.setUsername(resultSet.getString("username"));
                user.setFirstName(resultSet.getString("first_name"));
                user.setLastName(resultSet.getString("last_name"));
                user.setPassword(resultSet.getString("password"));
                users.add(user);
            }

        }catch (SQLException e) {
            e.printStackTrace();
        }
        return users;
    }

    public Long getIdUserByUsername(String username){
        Long id = null;
        try{
            PreparedStatement preparedStatement = connection.prepareStatement("SELECT * FROM users WHERE username = ?");
            preparedStatement.setString(1, username);
            ResultSet resultSet = preparedStatement.executeQuery();
            if(resultSet.next())
                return resultSet.getLong("id");

        }catch (SQLException e) {
            e.printStackTrace();
        }
        return id;
    }
}
