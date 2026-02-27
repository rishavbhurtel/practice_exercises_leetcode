"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

from collections import Counter


def canConstruct(ransomNote, magazine):
    note_dict = Counter(ransomNote)
    print(note_dict)
    magazine_dict = Counter(magazine)
    print(magazine_dict)

    for key, value in note_dict.items():
        if key in magazine_dict and value <= magazine_dict[key]:
            pass
        else:
            return False

    return True


ransomNote = "abcd"
magazine = "aabbcc"
yo = canConstruct(ransomNote, magazine)
print(yo)
