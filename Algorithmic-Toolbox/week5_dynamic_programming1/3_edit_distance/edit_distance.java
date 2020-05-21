import java.util.*;
import java.io.*;
class EditDistance {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String s = in.nextLine();
		String[] a = s.split(" ");
		int d = EditDistance(a[0], a[1]);
		System.out.println(d);
	}
	public static int EditDistance(String a, String b) {
		int m = a.length();
		int n = b.length();
		int[][] D = new int[m][n];
		for (int i = 0; i < m; i++)
			D[i][0] = i;
		for (int i = 0; i < n; i++)
			D[0][i] = i;
		for (int j = 1; j < n; j++) {
			for (int i = 1; i < m; i++) {
				int ins = D[i][j-1] + 1;
				int del = D[i-1][j] + 1;
				int match = D[i-1][j-1];
				int mis = D[i-1][j-1] + 1;
				if (a.charAt(i) == b.charAt(j)) 
					D[i][j] = Math.min(ins, Math.min(del, match));
				else
					D[i][j] = Math.min(ins, Math.min(del, mis));
			}
		}
		return D[m - 1][n - 1];
	}
}
