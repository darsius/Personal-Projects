package socialnetwork.domain;

import java.util.Date;
import java.util.UUID;

public class FriendRequest extends Entity<Long>{
    private Long senderId;
    private Long receiverId;
    private Date date;

    public FriendRequest(){}

    public FriendRequest(Long senderId, Long receiverId, Date date) {
        this.senderId = senderId;
        this.receiverId = receiverId;
        this.date = date;
        Long id = UUID.randomUUID().getMostSignificantBits() & Long.MAX_VALUE;
        this.setId(id);
    }

    public Long getSenderId(){
        return senderId;
    }

    public void setSenderId(Long senderId){
        this.senderId = senderId;
    }

    public Long getReceiverId(){
        return receiverId;
    }

    public void setReceiverId(Long receiverId){
        this.receiverId = receiverId;
    }

    public Date getDate(){
        return date;
    }

    public void setDate(Date date){
        this.date = date;
    }



//    @Override
//    public boolean equals(Object o) {
//        if (this == o) return true;
//        if (o == null || getClass() != o.getClass()) return false;
//        FriendRequest friendRequest = (FriendRequest) o;
//        return Objects.equals(user1, friendRequest.user1) && Objects.equals(fr, friendship.user2);
//    }
}
