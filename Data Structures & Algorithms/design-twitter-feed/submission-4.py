class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        minHeap = []
        followees = self.follows[userId] if userId in self.follows else set()
        followees.add(userId)
        for f in followees:
            if f in self.tweets:
                idx = len(self.tweets[f]) - 1
                time, tId = self.tweets[f][idx]
                minHeap.append((-time, tId, f, idx - 1))
        heapq.heapify(minHeap)

        while minHeap and len(feed) < 10:
            time, tId, f, idx = heapq.heappop(minHeap)
            feed.append(tId)

            if idx >= 0:
                time, tId = self.tweets[f][idx]
                heapq.heappush(minHeap, (-time, tId, f, idx - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows or followeeId not in self.follows[followerId]:
            return
        
        self.follows[followerId].remove(followeeId)
        
