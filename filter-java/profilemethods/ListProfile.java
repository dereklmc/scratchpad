package profilemethods;

import java.util.List;


public abstract class ListProfile extends ProfileMethod {

	protected List<Integer> items;

	public ListProfile(String name, List<Integer> items) {
		super(name);
		this.items = items;
	}
	
}