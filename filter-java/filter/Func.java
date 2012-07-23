package filter;
public interface Func<S,R> {

    public abstract R apply(S source);

}
