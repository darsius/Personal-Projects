package socialnetwork.domain.validators;

import socialnetwork.domain.User;

public class UserValidator implements Validator<User> {
    /**
     *
     * @param entity
     * @throws ValidationException
     */
    @Override
    public void validate(User entity) throws ValidationException {
        validateFirstName(entity.getFirstName());
        validateLastName(entity.getLastName());
        validate_username(entity.getUsername());
    }

    /**
     *
     * @param firstName
     * @throws ValidationException
     */
    private void validateFirstName(String firstName) throws ValidationException {
        if(firstName == null)
            throw new ValidationException("Prenumele trebuie sa fie diferit de null!");
        if(firstName.length() >= 20)
            throw new ValidationException("Prenumele e prea lung!");
    }

    /**
     *
     * @param lastName
     * @throws ValidationException
     */
    private void validateLastName(String lastName) throws ValidationException {
        if(lastName == null)
            throw new ValidationException("Numele trebuie sa fie diferit de null!");
        if(lastName.length() >= 20)
            throw new ValidationException("Numele prea lung");
    }
    private void validate_username(String username) throws ValidationException {
        if(username == null)
            throw new ValidationException("Username trebuie sa fie diferit de null!");
        if(username.length() >= 20)
            throw new ValidationException("Username prea lung");
    }
}
