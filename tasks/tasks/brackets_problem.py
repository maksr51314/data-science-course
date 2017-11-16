BRACKETS = {
    '(': ')',
    '{': '}',
    "[": ']'
}

#
# def check_brackets(s):
#     """ Check brackets
#
#     >>>check_brackets('()')
#     False
#
#     # >>>check_brackets("(()")
#     # False
#     # >>>check_brackets("()[]{}")
#     # True
#     """
#     if len(s) == 0:
#         return True
#
#     for brake in BRACKETS.keys():
#         if brake in s:
#             for indexStart, elStart in enumerate(s):
#                 if elStart == brake:
#                     for endIndex, el in enumerate(s[::-1]):
#                         if el == BRACKETS[brake]:
#                             return check_brackets(s[indexStart + 1:-endIndex - 1])
#                     break
#         else:
#             return False


def check_brackets(s, start=0):
    while start < len(s):
        bracket = s[start]
        if s[start] in BRACKETS:
            start = check_brackets(s, start)
        elif s[start] == BRACKETS[bracket]:
            return start
        else:
            start += 1
    return True

check_brackets('()')


