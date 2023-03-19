# python3
# Makars Sinakovs 221RDB519
def build_heap(data):
    swaps = []
    # TODO: Create heap and heap sort
    # try to achieve O(n) and not O(n^2)
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        j = i
        while True:
            left_child = j * 2 + 1
            right_child = j * 2 + 2
            if left_child < n and data[left_child] < data[j]:
                smallest_child = left_child
            else:
                smallest_child = j
            if right_child < n and data[right_child] < data[smallest_child]:
                smallest_child = right_child
            if smallest_child != j:
                data[j], data[smallest_child] = data[smallest_child], data[j]
                swaps.append((j, smallest_child))
                j = smallest_child
            else:
                break

    return swaps

def main():
    # TODO: add input and corresponding checks
    # add another input for I or F
    # first two tests are from keyboard, third test is from a file
    data = []
    n = 0
    text = input()
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in text:
        filen = input()
        with open(("./tests/" + filen), "r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
            assert len(data) == n
    # input from keyboard
    # checks if length of data is the same as the said length
    #assert len(data) == n

    # calls function to assess the data
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
