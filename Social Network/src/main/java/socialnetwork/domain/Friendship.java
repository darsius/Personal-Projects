package socialnetwork.domain;

import java.sql.Date;
import java.util.Objects;
import java.util.UUID;

public class Friendship extends Entity<Long>{
    private Long user1;
    private Long user2;
    private Date date;

    public Friendship(){};

    public Friendship(Long user1, Long user2, Date date) {
        this.user1 = user1;
        this.user2 = user2;
        this.date = date;
        Long id = UUID.randomUUID().getMostSignificantBits() & Long.MAX_VALUE;
        this.setId(id);
    }

    public Long getUtilizator1() {
        return user1;
    }

    public Long getUtilizator2() {return user2;}

    public void setUtilizator1(Long user1) {
        this.user1 = user1;
    }

    public void setUtilizator2(Long user2) {
        this.user2 = user2;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Friendship friendship = (Friendship) o;
        return Objects.equals(user1, friendship.user1) && Objects.equals(user2, friendship.user2);
    }

    @Override
    public int hashCode() {
        return Objects.hash(user1, user2);
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date){
        this.date = date;
    }
}
