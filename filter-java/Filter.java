import java.lang.Iterable;
import java.util.Iterator;

public class Filter<T> implements Iterable<T> {

    private static class FilterIterator<T> implements Iterator<T> {
        
        private final Iterator<T> it;
        private T next;
        
        public FilterIterator(Iterator<T> it) {
            this.it = it;
            next = advance();
        }
        
        @Override
        public boolean hasNext() {
            return next != null;
        }
        
        private T advance() {}
            while (it.hasNext()) {
                final T current = it.next();
                if (predicate.test(current)) {
                    return current;
                }
            }
            return null;
        }
        
        @Override
        public T next() {
            final T current = next;
            next = advance();
            return current;;
        }
        
        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
    }
    
    private Predicate<T> predicate;
    
    public Filter(Iterable<T> iter, Predicate<T> predicate) {
        this.predicate = predicate;
        this.iter = iter;
    }

    @Override
    public Iterator<T> iterator() {
        return new FilterIterator(iter.iterator());
    }
}
