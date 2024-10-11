# python3

def testing() :
    
    #Sample 1
    n_tables, n_queries = 5 , 5
    counts = [1,1,1,1,1]
    dstArr = [3,2,1,5,5]
    srcArr = [5,4,4,4,3]

    db = Database(counts)
    for i in range(n_queries):
        dst, src = dstArr[i],srcArr[i]
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)
    
    _ = input("Enter Enter to test Sample 2")

    #Sample 2
    n_tables, n_queries = 6 , 4
    counts = [10,0,5,0,3,3]
    dstArr = [6,6,5,4]
    srcArr = [6,5,4,3]

    db = Database(counts)
    for i in range(n_queries):
        dst, src = dstArr[i],srcArr[i]
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src) # destination ← symlink(destination)
        dst_parent = self.get_parent(dst) # source ← symlink(source)

        # Sets have been merged already if .
        if src_parent == dst_parent:
            return False
   
        # Merge two components
        if self.ranks[src_parent] >= self.ranks[dst_parent]:
            self.parents[src_parent] = dst_parent
        else :
            ### Use union by rank heuristic ###
            self.parents[dst_parent] = src_parent
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[src_parent] += 1

        self.row_counts[dst_parent] += self.row_counts[src_parent]
        self.row_counts[src_parent] = 0

        # update max_row_count with the new maximum table size
        if self.max_row_count < self.row_counts[dst_parent] :
            self.max_row_count = self.row_counts[dst_parent]

        return True

    def get_parent(self, table):
        ### Get symlink(table) ###

        # find parent and compress path
        parents_Update = []

        root = table
        while root != self.parents[root]:
            parents_Update.append(self.parents[root])
            root = self.parents[root]
        
        for i in parents_Update:
            self.parents[i] = root

        return root


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)

if __name__ == "__main__":
    main()
    ### Uncomment the below comment, if you need to run the the test.
    #testing()