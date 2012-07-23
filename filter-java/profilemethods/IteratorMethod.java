package profilemethods;

import java.util.List;

import filter.Filter;
import filter.Predicate;

public class IteratorMethod extends ListProfile {

	private final class IsEvenPredicate implements Predicate<Integer> {
		@Override
		public boolean test(final Integer i) {
			return i % 2 == 0;
		}
	}

	public IteratorMethod(final List<Integer> items) {
		super("Iterator", items);
	}

	@Override
	protected void runTest() {
		for (final Integer item : new Filter<Integer>(items,
				new IsEvenPredicate())) {
			System.out.println(item);
		}
	}

}