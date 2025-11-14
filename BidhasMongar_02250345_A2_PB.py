# Bubble Sort function
def bubble_sort(name_list):
    arr = name_list[:]    
    n = len(arr)

    # Outer loop for passes
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Insertion Sort function
def insertion_sort(score_list):
    arr = score_list[:]

    # Start from second element
    for i in range(1, len(arr)):
        current = arr[i]   # Value to insert
        j = i - 1

        # Move larger values one position forward
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the value into correct position
        arr[j + 1] = current
    return arr


# Quick Sort function
def quick_sort(arr, count):
    if len(arr) <= 1:
        return arr, count

    count += 1              
    pivot = arr[0]
    left = []               
    right = []              

    # Split into left and right lists
    for num in arr[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    # Recursively sort both sides
    left_sorted, count = quick_sort(left, count)
    right_sorted, count = quick_sort(right, count)

    # Combine results
    return left_sorted + [pivot] + right_sorted, count


# MAIN PROGRAM
def main():
    student_names = [
        "Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Sonam", "Pema",
        "Ugyen", "Dawa", "Chimi", "Yeshi", "Thinley", "Karma",
        "Tshering", "Wangmo"
    ]

    test_scores = [
        78, 45, 92, 67, 88, 54, 73, 82, 91, 59,
        76, 85, 48, 93, 71, 89, 57, 80, 69, 62
    ]

    book_prices = [
        450, 230, 678, 125, 890, 320, 540, 210,
        760, 480, 330, 999, 150, 275, 610
    ]

    print("=== Sorting Algorithms Menu ===")

    # Loop until user exits
    while True:
        print("\nChoose an option (1-4):")
        print("1. Bubble Sort - Student Names")
        print("2. Insertion Sort - Test Scores")
        print("3. Quick Sort - Book Prices")
        print("4. Exit Program")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Original Names:", student_names)
            sorted_names = bubble_sort(student_names)
            print("Sorted Names:", sorted_names)

        elif choice == "2":
            print("Original Scores:", test_scores)
            sorted_scores = insertion_sort(test_scores)
            print("Sorted Scores:", sorted_scores)

            print("Top 5 Scores:")
            top_five = sorted_scores[-5:][::-1]
            for i, score in enumerate(top_five, 1):
                print(f"{i}. {score}")

        elif choice == "3":
            print("Original Prices:", book_prices)
            sorted_prices, calls = quick_sort(book_prices, 0)
            print("Sorted Prices:", sorted_prices)
            print("Recursive Calls:", calls)

        elif choice == "4":
            print("Thank you for using the sorting program!")
            break

        else:
            print("Invalid option.")

        again = input("Perform another sort? (y/n): ").lower()
        if again != "y":
            print("Thank you for using the sorting program!")
            break
# Run the program
if __name__ == "__main__":
    main()
