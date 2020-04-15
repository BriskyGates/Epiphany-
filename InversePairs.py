class Solution:
    def InversePairs(self, data):
        """
        从小到大排好序后,始终从copy中取最小元素,然后求其在原数组中的位置,
        其前面就有多个个比它大的数字,再将其删除,确保后面遍历到的数全部都是比它大的数
        :param data:
        :return:
        """
        count = 0
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count

