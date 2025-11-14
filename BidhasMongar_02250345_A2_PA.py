# Function for Linear Search
def linear_search(id_list, target_id):
    comparisons = 0
    for index in range(len(id_list)):
        comparisons += 1
        if id_list[index] == target_id:
            return index + 1, comparisons
    return None, comparisons


# Function for Binary Search
def binary_search(score_list, target_score):
    left = 0                    
    right = len(score_list) - 1  
    comparisons = 0              
    while left <= right:
        mid = (left + right) // 2   
        comparisons += 1            
        if score_list[mid] == target_score:
            return mid + 1, comparisons
        elif target_score < score_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return None, comparisons


# MAIN PROGRAM
def main():
    # Hardcoded lists
    student_ids = [
        1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009,
        1007, 1012, 1015, 1006, 1011, 1013, 1014, 1000,
        1020, 1018, 1017, 1016
    ]

    sorted_scores = [
        45, 52, 58, 63, 67, 72, 75, 78, 82, 85,
        88, 90, 92, 95, 98, 99, 100, 102, 105, 110
    ]

    print("=== Searching Algorithms Menu ===")
    while True:
        print("\nChoose an option (1-3):")
        print("1. Linear Search ")
        print("2. Binary Search ")
        print("3. Exit Program")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Student ID List:", student_ids)
            target = int(input("Enter Student ID to search: "))
            
            position, comp = linear_search(student_ids, target)

            if position:
                print(f"Student ID {target} found at position {position}.")
            else:
                print(f"Student ID not found.")

        elif choice == "2":
            print("Sorted Scores:", sorted_scores)
            target = int(input("Enter Score to search: "))

            position,comp = binary_search(sorted_scores, target)
            if position:
                print(f"Score {target} found at position {position}.")
            else:
                print(f"Score not found.")
        elif choice == "3":
            print("Thank you for using the search program!")
            break
        else:
            print("Invalid option.")
        again = input("Perform another search? (y/n): ").lower()
        if again != "y":
            print("Thank you for using the search program!")
            break
# Run the main program
if __name__ == "__main__":
    main()