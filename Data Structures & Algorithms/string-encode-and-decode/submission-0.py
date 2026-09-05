class Solution:
    def encode(self, strs: List[str]) -> str:
        str_concat = ""
        for i in strs:
            str_concat += str(len(i)) + "#" + i
        return str_concat

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start_word = j + 1
            end_word = start_word + length

            res.append(s[start_word:end_word])

            i = end_word

        return res
