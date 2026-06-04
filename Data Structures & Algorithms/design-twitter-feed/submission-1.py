class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = {}

        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append((-self.count, tweetId))
        else:
            self.tweets[userId] = [(-self.count, tweetId)]
        
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        minHeap = []
        followees = self.follows.get(userId, set()) | {userId}
        for f in followees:
            if f in self.tweets:
                idx = len(self.tweets[f]) - 1
                count, tId = self.tweets[f][idx]
                minHeap.append((count, tId, f, idx - 1))
        heapq.heapify(minHeap)

        while minHeap and len(feed) < 10:
            count, tId, fId, idx = heapq.heappop(minHeap)
            feed.append(tId)

            if idx >= 0:
                count, tId = self.tweets[fId][idx]
                heapq.heappush(minHeap, (count, tId, fId, idx - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            return
        
        self.follows[followerId].discard(followeeId)