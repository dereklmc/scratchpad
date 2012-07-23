package profilemethods;

import java.util.List;

public class IndexedMethod extends ListProfile {

	public IndexedMethod(List<Integer> items) {
		super("Indexed Method", items);
		// TODO Auto-generated constructor stub
	}

	@Override
	protected void runTest() {
		for (int i = 0; i < items.size(); i++) {
			Integer item = items.get(i);
			if (item % 2 == 0) {
				System.out.println(item);
			}
		}

	}

}