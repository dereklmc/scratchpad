package profilemethods;

public abstract class ProfileMethod {
	
	private String name;
	private long start = 0;
	private long end = 0;
	
	public ProfileMethod(String name) {
		this.name = name;
	}
	
	public boolean run() {
		start = System.nanoTime();
		runTest();
		end = System.nanoTime();
		return true;
	}
	
	protected abstract void runTest();
	
	public long timeDiff() {
		return end - start;
	}
	
	public void printTiming() {
		System.out.println(name + ": " +timeDiff());
	}

	public String getName() {
		return name;
	}
}