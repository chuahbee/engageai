def kmp_search(text, pattern):
    if not text or not pattern:
        return -1  # 提前退出，避免 len(None)
    
    def build_next(pattern):
        next = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = next[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            next[i] = j
        return next

    next = build_next(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = next[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return True  # 匹配成功
    return False
