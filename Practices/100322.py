class Solution:
    def clearStars(self, string):
        se = set()
        for j, i in enumerate(string):
            if i == '*':
                p = next(iter(se))
                id = p[1]
                string = string[:id] + '*' + string[id+1:]
                se.remove(p)
            else:
                se.add((i, -j))

        r = ""
        for i in string:
            if i != '*':
                r += i
        return r

