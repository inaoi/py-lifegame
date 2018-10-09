class ListHelper:

    @staticmethod
    def _fill(target, count, fillData, fillFront=False):
        diffCount = count - len(target)
        if diffCount <= 0:
            return target

        appendData = [fillData] * diffCount
        if fillFront:
            target[:0] = appendData
        else:
            target[len(target):] = appendData

        return target

    @staticmethod
    def _slice(target, index, count):
        return target[index:index + count]
