package socialnetwork.utils.events;

import socialnetwork.domain.User;

public class ChangeEvent<E> implements Event {
    private ChangeEventType type;
    private E entity;

    public ChangeEvent(ChangeEventType type, E entity) {
        this.type = type;
        this.entity = entity;
    }

    public ChangeEventType getType() {
        return type;
    }


    public E getEntity() {
        return entity;
    }
}