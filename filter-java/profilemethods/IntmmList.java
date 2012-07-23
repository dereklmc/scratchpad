package profilemethods;
import java.util.ArrayList;
import java.util.List;



public class IntmmList extends ListProfile {

	public IntmmList(List<Integer> items) {
		super("Intermediate List", items);
	}

	@Override
	protected void runTest() {
		final List<Integer> filteredItems = new ArrayList<Integer>();
		for (Integer item : items) {
			if (item % 2 == 0) {
				filteredItems.add(item);
			}
		}

		for (Integer item : filteredItems) {
			System.out.println(item);
		}
	}
	
}