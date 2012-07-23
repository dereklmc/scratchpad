import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import profilemethods.AnonPredIteratorMethod;
import profilemethods.ForEachMethod;
import profilemethods.IndexedMethod;
import profilemethods.IntmmList;
import profilemethods.IteratorMethod;
import profilemethods.ListProfile;
import profilemethods.ProfileMethod;

public class Driver {
	
	public static void main(String[] args) throws IOException {
		System.out.print("Number of Items? ");
		Scanner s = new Scanner(System.in);
		int numItems = Integer.parseInt(s.nextLine());
		final List<Integer> items = new ArrayList<Integer>();
		for (int i = 0; i < numItems; i++) {
			items.add(i);
		}

		List<ListProfile> methods = new ArrayList<ListProfile>();
		methods.add(new AnonPredIteratorMethod(items));
		methods.add(new IteratorMethod(items));
		methods.add(new ForEachMethod(items));
		methods.add(new IntmmList(items));
		methods.add(new IndexedMethod(items));

		for (ListProfile m : methods) {
			m.run();
		}
		
		for (ListProfile m : methods) {
			m.printTiming();
		}
		
		for (ListProfile a : methods) {
			for (ListProfile b : methods) {
				if (a != b) {
					printRatio(a,b);
				}
			}
		}
	}
	
	public static void printRatio(ProfileMethod a, ProfileMethod b) {
		System.out.println("======");
		System.out.println(a.getName() + " VS " + b.getName());
		System.out.println((float) a.timeDiff() /  (float) b.timeDiff());
		System.out.println("======");
	}

}
