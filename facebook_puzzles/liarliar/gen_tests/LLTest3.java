/* usage: java LLTest3 n */
class LLTest3 {
public static void main(String[] args) {
int n = Integer.parseInt(args[0]) & ~1;
java.io.PrintWriter out = new java.io.PrintWriter(new java.io.BufferedWriter(new java.io.OutputStreamWriter(System.out)));
out.printf("%d\n", n);
for(int i = 0; i < n; ++i) {
out.printf("%d\t%d\n%d\n", i, 1, (i + 1) % n);
}
out.close();
}
}
