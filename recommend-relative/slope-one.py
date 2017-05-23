# coding=utf-8
import codecs

users = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
         "Ben": {"Taylor Swift": 5, "PSY": 2},
         "Clara": {"PSY": 3.5, "Whitney Houston": 4},
         "Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}

myScore = {'Snakes on a Plane': 3.0, 'Forest Gump': 5.0, 'Jaws': 1.0, 'Napolean Dynamite': 3.0, 'Toy Story': 4.0}


def loadMovieDB(path=''):
    data = {}
    user_rating = {}
    i = 0
    f = codecs.open(path + "Movie_Ratings.csv", )
    for line in f:
        i = i + 1
        if i == 1:
            lists = line.split(',')
            lists.pop(0)
            user_ids = []
            for user in lists:
                user = user.strip('"').strip('"\n')
                user_ids.append(user)
                user_rating[user] = {}
        else:
            next_line = line.split(',')
            movie_name = next_line.pop(0).strip('"')
            scores = {}
            array = []
            for k in next_line:
                k = k.strip().strip('\n')
                array.append(k)
            scores[movie_name] = array
            for n in user_ids:
                index = user_ids.index(n)
                if scores[movie_name][index] == '':
                    continue
                else:
                    user_rating[n].update({movie_name: float(scores[movie_name][index])})
                    data[n] = user_rating[n]
    f.close()
    return data


data = loadMovieDB('/home/dujinqiao/Documents/python-practise/')

print data


class Recommender:
    def __init__(self, data):
        self.data = data
        self.frequencies = {}
        self.deviations = {}

    # 计算偏差
    def computeDeviations(self):
        # 遍历每个用户对乐队的打分信息
        for ratings in self.data.values():
            # print ratings
            # 遍历乐队中的每支乐队
            for (item, rating) in ratings.items():
                # 给字典 frequencies deviations中添加项
                # 如果没有这个乐队名，给 frequencies 添加 frequencies = {乐队名：{}}，同理， deviations = {乐队名：{}}
                self.frequencies.setdefault(item, {})
                self.deviations.setdefault(item, {})
                # print self.frequencies
                # print self.deviations
                # 遍历乐队中的每支乐队
                for (item2, rating2) in ratings.items():
                    # 如果这次遍历的乐队名不是外层的乐队名，依次计算与外层乐队名的偏差
                    if item != item2:
                        # 如果 frequencies[乐队名]={}， 将 frequencies[乐队名]={乐队名2:0}
                        # 同理， deviations[乐队名] = {乐队名2:0.0}
                        self.frequencies[item].setdefault(item2, 0)
                        # print self.frequencies
                        self.deviations[item].setdefault(item2, 0.0)
                        # print self.deviations
                        # 如果 frequencies[乐队名]！={}，也就是说，以后依次遍历乐队名时，将 item2 的值累加
                        self.frequencies[item][item2] += 1
                        # print self.frequencies
                        self.deviations[item][item2] += rating - rating2
                        # print self.deviations
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
        # 计算出最后得分
        for (item, value) in recommendations.items():
            recommendations[item] = value / frequencies[item]
            # print recommendations

        return sorted(recommendations.items(), key=lambda d: d[1], reverse=True)


#
# r = Recommender(users)
# userRating = users['Ben']
# recommend = r.slopeOneRecommendations(userRating)

my = Recommender(data)
print my.computeDeviations()
myRecommend = my.slopeOneRecommendations(myScore)
print myRecommend

# 最终推荐的影片[('Star Wars', 4.494623655913978), ('Shawshank Redemption', 4.42),
#  ('The Dark Knight', 4.375), ('The Matrix', 4.021505376344086), ('Gladiator', 3.8701298701298703)]
