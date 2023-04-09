package socialnetwork.domain.validators;
import socialnetwork.domain.Friendship;

import java.util.Objects;

public class FriendshipValidator implements Validator<Friendship>{
    /**
     *
     * @param entity
     * @throws ValidationException
     */
    @Override
    public void validate(Friendship entity) throws ValidationException {
//        if (entity.getUtilizator1() == entity.getUtilizator2().getId())
//            throw new ValidationException("Prietenii nu pot avea acelasi ID!");
//        if (Objects.equals(entity.getUtilizator1().getUsername(), entity.getUtilizator2().getUsername()))
//            throw new ValidationException("Prietenii nu pot avea acelasi username!");
    }
}
