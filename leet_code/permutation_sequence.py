import math
class Solution(object):

    def getPermutation(self, n, k):
        seq = list()
        nums = []
        for i in (range(1, n + 1)):
            nums.append(str(i))

        fac_n = n - 1
        step = math.factorial(fac_n)
        while True:
            while k // step == 0:
                seq_item = nums.pop(0)
                seq.append(seq_item)
                k = k % step
                fac_n = fac_n - 1
                step = math.factorial(fac_n)

            if k % step != 0:
                index = k // step
                seq.append(nums.pop(index))
                k = k % step
                fac_n = fac_n - 1
                step = math.factorial(fac_n)
                continue

            if k % step == 0:
                idx = k // step
                seq_item = nums.pop(idx - 1)
                seq.append(seq_item)
                seq.extend(list(reversed(nums)))
                break

        return "".join(seq)

if __name__ == "__main__":

    s = Solution()
    assert (s.getPermutation(4, 5) == "1423")
    assert(s.getPermutation(4, 6) == "1432")
    assert(s.getPermutation(4, 8) == "2143")
    assert(s.getPermutation(4, 9) == "2314")
    assert (s.getPermutation(4, 11) == "2413")
    assert(s.getPermutation(1, 1) == "1")













