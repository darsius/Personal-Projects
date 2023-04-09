package socialnetwork.domain;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.UUID;

public class User extends Entity<Long>{
    private String firstName;
    private String lastName;
    private String username;
    private String password;
    private Map<Long, User> friends;

    public User(){}

    public User(String firstName, String lastName, String username, String password) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.username = username;
        this.password = password;
        friends = new HashMap<>();
        Long id = UUID.randomUUID().getMostSignificantBits() & Long.MAX_VALUE;
        this.setId(id);
    }

    public String getFirstName() {return firstName;}

    public void setFirstName(String firstName) {this.firstName = firstName;}

    public String getLastName() {return lastName;}

    public void setLastName(String lastName) {this.lastName = lastName;}

    public String getUsername() {return username;}

    public void setUsername(String username) {this.username = username;}

    public Iterable<User> getFriends() {return friends.values();}

    @Override
    public String toString() {
        return "Utilizatorul: " +
                "\nId: " + id +
                "\nPrenumele: " + firstName  +
                ",\nNumele: " + lastName  +
                ",\nusername-ul: " + username +
                "\nparola: " + password;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof User)) return false;
        User that = (User) o;
        return id.equals(that.getId());
    }

    @Override
    public int hashCode() {return Objects.hash(getFirstName(), getLastName(), getUsername());}

    public void addFriend(User u) {friends.put(u.id, u);}

    public boolean removeFriend(User u) {
        return friends.remove(u.id) != null;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}