package profilemethods;

import java.util.List;

import filter.Filter;
import filter.Predicate;



public class AnonPredIteratorMethod extends ListProfile {

	public AnonPredIteratorMethod(final List<Integer> items) {
		super("Iterator W/ Anon Predicate", items);
	}

	@Override
	protected void runTest() {
		for (final Integer item : new Filter<Integer>(items,
				new Predicate<Integer>() {
					@Override
					public boolean test(final Integer i) {
						return i % 2 == 0;
					}
				})) {
			System.out.println(item);
		}
	}
	
}