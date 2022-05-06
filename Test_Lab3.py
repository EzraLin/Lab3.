import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 10, 89, 45]
    test_arr = [10, 11, 12, 22, 25, 34, 45, 64, 89, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 1, 2, 3]
    test_arr = [90, 64, 34, 25, 22, 12, 11, 3, 2, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 9, 8, 10]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])
def test_bubble_sort_morethan10():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 3, 4, 5, 6, 7]

    result = Lab3.bubble_sort(input_arr, 0)

    assert (result == 1)
def test_bubble_sort_lessthan10():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 0)

    assert (result == 2)
def test_bubble_sort_zero():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, 0)

    assert (result == 0)
def test_bubble_sort_not_int():
    result = []
    input_arr = [1, 2, 3, 4, 5, 'a']

    result = Lab3.bubble_sort(input_arr, 0)

    assert (result == 3)