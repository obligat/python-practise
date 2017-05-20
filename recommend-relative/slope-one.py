# coding=utf-8
users = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
         "Ben": {"Taylor Swift": 5, "PSY": 2},
         "Clara": {"PSY": 3.5, "Whitney Houston": 4},
         "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}


class Recommender:
    def __init__(self, data):
        self.data = data
        self.frequencies = {}
        self.deviations = {}
        pass

    # 计算偏差
    def computeDeviations(self):
        # 遍历每个用户对乐队的打分信息
        for ratings in self.data.values():
            print ratings
            # 遍历乐队中的每支乐队
            for (item, rating) in ratings.items():
                # 给字典 frequencies deviations中添加项
                # 如果没有这个乐队名，给 frequencies 添加 frequencies = {乐队名：{}}，同理， deviations = {乐队名：{}}
                self.frequencies.setdefault(item, {})
                self.deviations.setdefault(item, {})
                print self.frequencies
                print self.deviations
                # 遍历乐队中的每支乐队
                for (item2, rating2) in ratings.items():
                    # 如果这次遍历的乐队名不是外层的乐队名，依次计算与外层乐队名的偏差
                    if item != item2:
                        # 如果 frequencies[乐队名]={}， 将 frequencies[乐队名]={乐队名2:0}
                        # 同理， deviations[乐队名] = {乐队名2:0.0}
                        self.frequencies[item].setdefault(item2, 0)
                        print self.frequencies
                        self.deviations[item].setdefault(item2, 0.0)
                        print self.deviations
                        # 如果 frequencies[乐队名]！={}，也就是说，以后依次遍历乐队名时，将 item2 的值累加
                        self.frequencies[item][item2] += 1
                        print self.frequencies
                        self.deviations[item][item2] += rating - rating2
                        print self.deviations

        # 遍历 deviations 字典，deviations = {item:{item2:偏差之和}}，
        # frequencies = {item: {item2: 共同对 item item2 打分的用户数}}
        for (item, ratings) in self.deviations.items():
            for item2 in ratings:
                # 将 、偏差之和、 替换为 、除以共同打分的用户数之后的偏差、
                ratings[item2] /= self.frequencies[item][item2]

    def slopeOneRecommendations(self, userRatings):
        recommendations = {}
        frequencies = {}
        # 遍历 userRatings 中的每一项，userRatings 为用户打过分的所有乐队
        for (userItem, userRating) in userRatings.items():
            # 遍历 deviations 里的每一项
            for (diffItem, diffRatings) in self.deviations.items():
                # 如果这个乐队（diffItem）该用户未打过分，并且 diffItem 和 userItem 存在偏差值，即可以推荐 diffItem 给用户
                if diffItem not in userRatings and userItem in self.deviations[diffItem]:
                    # freq 存的是共同对 diffItem userItem 打分的用户数
                    freq = self.frequencies[diffItem][userItem]
                    # recommendations = {diffItem: 0.0}  frequencies = {diffItem: 0}
                    recommendations.setdefault(diffItem, 0.0)
                    frequencies.setdefault(diffItem, 0)
                    #  recommendations[diffItem] = 分子   requencies[diffItem] = 分母
                    recommendations[diffItem] += (diffRatings[userItem] + userRating) * freq
                    frequencies[diffItem] += freq
        # recommendations = [(self.convertProductID2name(k),
        #                     v / frequencies[k])
        #                    for (k, v) in recommendations.items()


r = Recommender(users)
r.computeDeviations()
print (r.deviations)
