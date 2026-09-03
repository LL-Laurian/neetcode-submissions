class Twitter:

    def __init__(self):
        self.tweets = []
        self.usersFollow = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (userId, tweetId)

        self.tweets.append(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        following = []
        if userId in self.usersFollow:
            following = self.usersFollow[userId]

        res = []
        
        n = len(self.tweets)
        count = 0

        for i in range(n-1, -1, -1):
            if count == 10:
                return res
            if self.tweets[i][0] == userId or self.tweets[i][0] in following:
                res.append(self.tweets[i][1])
                count+=1
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.usersFollow[followerId].add(followeeId)      

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usersFollow[followerId].discard(followeeId)
