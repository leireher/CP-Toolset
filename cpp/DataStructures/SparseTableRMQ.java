public class SparseTableRMQ {

    private final int a[], logTable[], rmq[][];

    public SparseTableRMQ(int[] a) {
        final int n = a.length;
        this.a = a;
        this.logTable = new int[n+1];
        for (int i = 2; i <= n; i++) logTable[i] = logTable[i>>1] + 1;
        this.rmq = new int[logTable[n]+1][n];
        for (int i = 0; i < n; i++) rmq[0][i] = i;
        for (int k = 1; (1<<k) < n; k++) {
            for (int i = 0; i+(1<<k) <= n; i++) {
                final int x = rmq[k-1][i], y = rmq[k-1][i+(1<<k-1)];
                rmq[k][i] = a[x] <= a[y] ? x : y;
            }
        }
    }

    public int minPos(int i, int j) { // Both inclusive
        final int k = logTable[j-i], x = rmq[k][i], y = rmq[k][j-(1<<k)+1];
        return a[x] <= a[y] ? x : y;
    }
    
    public int minVal(int i, int j) { // Both inclusive
        final int k = logTable[j-i];
        return Math.min(a[rmq[k][i]], a[rmq[k][j-(1<<k)+1]]);
    }
    
}
