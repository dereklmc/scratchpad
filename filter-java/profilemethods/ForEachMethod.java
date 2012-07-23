package profilemethods;
import java.util.List;



public class ForEachMethod extends ListProfile {

	public ForEachMethod(List<Integer> items) {
		super("For Each Method", items);
	}

	@Override
	protected void runTest() {
		for (Integer item : items) {
			if (item % 2 == 0) {
				System.out.println(item);
			}
		}
		
	}
}