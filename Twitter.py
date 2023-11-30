from typing import *
import heapq

class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweets[userId].append([self.time, tweetId])
        if userId not in self.followers:
            self.followers[userId] = {userId}

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        for fId in self.followers[userId]:
            minHeap += self.tweets[fId]
        heapq.heapify(minHeap)
        ans = []
        k = 0
        while minHeap and k < 10:
            k += 1
            ans.append(heapq.heappop(minHeap)[1])

        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = {followerId}
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)



"""
["Twitter","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
[[],[1,1],[1],[2,1],[2],[2,1],[2]]
"""
tw = Twitter()
tw.postTweet(1,1)
tw.getNewsFeed(1)
tw.follow(2,1)
tw.getNewsFeed(2)
tw.unfollow(2,1)
tw.getNewsFeed(2)
