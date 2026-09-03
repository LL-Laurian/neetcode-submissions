class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)
        self.usersFollow = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweetMap[userId][:]
        for followeeId in self.usersFollow[userId]:
            feed.extend(self.tweetMap[followeeId])

        feed.sort(key=lambda x: -x[0])
        return [tweetId for _, tweetId in feed[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.usersFollow[followerId].add(followeeId)      

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usersFollow[followerId].discard(followeeId)
