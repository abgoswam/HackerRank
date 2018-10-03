class FriendGroups:
    def __init__(self, n):
        self.total_people = n
        self.parent = [-1 for _ in range(n)]
        self.group_count = n

    def find(self, v):
        while self.parent[v] != -1:
            v = self.parent[v]
        return v

    # O(log n) with balanced trees
    # O(log*n) ~ O (constant), if we apply Robert Tarjan's path compression trick:
    # -- https://en.wikipedia.org/wiki/Proof_of_O(log*n)_time_complexity_of_union%E2%80%93find
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            self.group_count -= 1

    # O(1). just return group_count
    def get_group_count(self):
        return self.group_count

    # hard problem, the Union-Find data structure doesnt support this
    # reason : (i, j) are no longer friends, but that doesn't mean group has split
    def remove_friends(self, i, j):
        pass


# test and verify
if __name__ == "__main__":
    N = 5
    friend_groups = FriendGroups(N)
    print(friend_groups.get_group_count())
    # lets add some friendship's shall we ?
    friend_groups.union(0, 1)
    friend_groups.union(2, 3)
    print(friend_groups.get_group_count())
    # friendship grows!
    friend_groups.union(0, 3)
    print(friend_groups.get_group_count())
    # lets all be friends :)
    friend_groups.union(2, 4)
    print(friend_groups.get_group_count())


