class Twitter:

    def __init__(self):
        self.follower_dict = defaultdict(set)
        self.tweets_dict = OrderedDict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_dict[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        output = []
        i = 0
        for key, value in reversed(self.tweets_dict.items()):
            if value in self.follower_dict[userId] or value == userId:
                output.append(key)
                i += 1
            if i >= 10:
                break
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower_dict[followerId]:
            self.follower_dict[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
