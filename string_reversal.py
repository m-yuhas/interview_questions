#!/usr/bin/env python


def reversal(s: str) -> str:
    """Reverse a string such that s[n] = s[len(s) - 1 -  n]
    for 0 < n < len(s) / 2.

    This function can run in O(n) time.  Although the actual reversal is
    performed in place, the function returns a new string.

    Arguments:
        s : str
            input string

    Returns:
        str: the reversed string
    """
    s = list(s)
    for i in range(int(len(s)/2)):
        temp = s[i]
        s[i] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = temp
    return ''.join(s)


def sentence_reversal(s: str) -> str:
    """Reverse the order of words in a sentence ignoring punctuation.

    This function can run in O(n) time. Because Python requires returning a new
    copy of a string and not a pointer this function does not technically
    perform the operation in place.

    Arguments:
        s : str
            input sentence

    Returns:
        str: the sentence with the order of words reversed
    """
    s = reversal(s).split()
    for i in range(len(s)):
        s[i] = reversal(s[i])
    return ' '.join(s)


def sentence_reversal_with_punctuation(s: str) -> str:
    """Reverse the order of words in a sentence and preserve the sentence's
    punction mark.

    This function can run in O(n) time.  Because Python requires returning a
    new copy of a string and not a pointer, this function does not technically
    perform the operation in place.

    Arguments:
        s : str
            input sentence

    Return:
        str: the sentence with the word order reversed and punctuation
            preserved
    """
    s = list(s)
    s[0] = s[0].lower()
    valid_punctuation = ['.', '?', '!']
    mark = ''
    if s[-1] in valid_punctuation:
        mark = s[-1]
        s = s[:-1]
    s = reversal(''.join(s)).split()
    for i in range(len(s)):
        s[i] = reversal(s[i])
    s = ' '.join(s) + mark
    s = list(s)
    s[0] = s[0].upper()
    return ''.join(s)


def paragraph_reversal(p: str) -> str:
    """Reverse the order of sentences in a paragraph.

    This function can run in O(n) time.  Because Python requires returning a
    new copy of a string and not a pointer, this function does not technically
    perform the operation in place.

    Arguments:
        p : str
            input paragraph

    Returns:
        str: the paragraph with the order of sentences reversed
    """
    sentence_breaks = ['.', '?', '!']
    sentences = []
    sentence = []
    state = 'normal_text'
    for i in range(len(p)):
        if state == 'normal_text':
            sentence.append(p[i])
            if p[i] in sentence_breaks:
                state = 'punctuation'
        elif state == 'punctuation':
            sentence.append(p[i])
            if p[i].strip() != '':
                state = 'normal_text'
            else:
                state = 'white_space'
        elif state == 'white_space':
            if p[i].strip() == '':
                continue
            elif p[i].upper() == p[i]:
                sentences.append(''.join(sentence))
                sentence = [p[i]]
            state = 'normal_text'
    if sentence[-1].strip != '':
        sentences.append(' ')
    sentences.append(''.join(sentence))
    for i in range(int(len(sentences)/2)):
        temp = sentences[i]
        sentences[i] = sentences[len(sentences) - 1 - i]
        sentences[len(sentences) - 1 - i] = temp
    return ''.join(sentences)
    

if __name__ == '__main__':
    # Problem 1:
    # Write a function that takes a string and reverses the order of its
    # characters.
    print('Problem #1:\n{}'.format(reversal("Hello World!")))

    # Problem 2:
    # Write a function that takes a sentence and reverses the order of its
    # words.  (Ignore punctuation for this problem.)
    print('Problem #2:\n{}'.format(
        sentence_reversal("The quick brown fox jumped over the lazy dog.")))


    # Problem 3:
    # Write a function that takes a sentence and reverses the order of its
    # words.  The punctuation at the end of the sentence must be preserved as
    # well as a capital letter at the beginning of the sentence.
    print('Problem #3:\n{}'.format(
        sentence_reversal_with_punctuation(
            "The quick brown fox jumped over the lazy dog.")))
    
    # Problem 4:
    # Write a function that takes a paragraph (string containing multiple
    # sentences) and reverses the order of the sentences, preserving their
    # original punctuation.
    print('Problem #4:\n{}'.format(
        paragraph_reversal(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
            "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut "
            "enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor "
            "in reprehenderit in voluptate velit esse cillum dolore eu "
            "fugiat nulla pariatur. Excepteur sint occaecat cupidatat non "
            "proident, sunt in culpa qui officia deserunt mollit anim id est "
            "laborum.")))
