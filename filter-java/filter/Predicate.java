package filter;

public interface Predicate<T> {
    
    public boolean test(T current);
    
}
