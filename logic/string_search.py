import time


class StringSearchAlgorithms:

    def naive_search(self, text, pattern):
        """Naive pattern searching."""
        start_time = time.perf_counter()
        m = len(pattern)
        n = len(text)
        indices = []

        for i in range(n - m + 1):
            if text[i:i + m] == pattern:
                indices.append(i)

        end_time = time.perf_counter()
        return indices, (end_time - start_time)

    def rabin_karp(self, text, pattern):
        """Rabin-Karp algorithm using rolling hash."""
        start_time = time.perf_counter()
        d = 256
        q = 101
        m = len(pattern)
        n = len(text)
        p = 0
        t = 0
        h = 1
        indices = []

        if m > n: return [], 0

        for i in range(m - 1):
            h = (h * d) % q

        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q

        for i in range(n - m + 1):
            if p == t:
                if text[i:i + m] == pattern:
                    indices.append(i)

            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                if t < 0: t = t + q

        end_time = time.perf_counter()
        return indices, (end_time - start_time)

    def kmp_search(self, text, pattern):
        """Knuth-Morris-Pratt algorithm[cite: 63]."""
        start_time = time.perf_counter()

        def compute_lps(pat, m, lps):
            length = 0
            i = 1
            lps[0] = 0
            while i < m:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1

        m = len(pattern)
        n = len(text)
        lps = [0] * m
        indices = []

        compute_lps(pattern, m, lps)

        i = 0
        j = 0
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == m:
                indices.append(i - j)
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        end_time = time.perf_counter()
        return indices, (end_time - start_time)