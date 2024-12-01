# Problem 1: Discount Calculation
def compute_discount(quantity, price, discount_rate):
    # Compute the discount amount and the discounted price
    discount_amount = quantity * price * (discount_rate / 100)
    discounted_price = quantity * price - discount_amount
    return discount_amount, discounted_price

# Problem 2: Student Exam Scores
def compute_scores(score1, score2, score3):
    total_points = score1 + score2 + score3
    average_score = total_points / 3
    return total_points, average_score

# Problem 3: Sales Commission and Target
def compute_commission_and_target(sales):
    if sales > 100000:
        commission = sales * 0.10  # 10% commission
    else:
        commission = sales * 0.05  # 5% commission
    target = sales * 0.05  # Next year's target is 5% of sales
    return commission, target

# Problem 4: Bowler's Score and Handicap
def compute_scores_with_handicap(game1, game2, game3, handicap):
    average_score = (game1 + game2 + game3) / 3
    average_with_handicap = average_score + handicap
    return average_score, average_with_handicap

# Problem 5: Global Variables for Total and Tax
total = 0
tax = 0

def compute_total_and_tax(quantity, unit_price):
    global total, tax
    total = quantity * unit_price
    tax = total * 0.07  # 7% tax

# Main function to gather inputs and call respective functions
def main():
    # Problem 1: Discount Calculation
    print("Problem 1: Discount Calculation")
    quantity = float(input("Enter the quantity: "))
    price = float(input("Enter the price per item: "))
    discount_rate = float(input("Enter the discount rate (in %): "))

    discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)
    print(f"Quantity: {quantity}, Price: {price}")
    print(f"Discount amount: {discount_amount}")
    print(f"Discounted price: {discounted_price}")
    print()

    # Problem 2: Student Exam Scores
    print("Problem 2: Student Exam Scores")
    last_name = input("Enter the student's last name: ")
    score1 = float(input("Enter score for exam 1: "))
    score2 = float(input("Enter score for exam 2: "))
    score3 = float(input("Enter score for exam 3: "))

    total_points, average_score = compute_scores(score1, score2, score3)
    print(f"Student's Last Name: {last_name}")
    print(f"Total Points: {total_points}")
    print(f"Average Score: {average_score:.2f}")
    print()

    # Problem 3: Sales Commission and Target
    print("Problem 3: Sales Commission and Target")
    salesperson_last_name = input("Enter salesperson's last name: ")
    sales = float(input("Enter the total sales amount: "))

    commission, target = compute_commission_and_target(sales)
    print(f"Salesperson: {salesperson_last_name}")
    print(f"Commission: {commission}")
    print(f"Next Year's Target: {target}")
    print()

    # Problem 4: Bowler's Score and Handicap
    print("Problem 4: Bowler's Score and Handicap")
    bowler_last_name = input("Enter bowler's last name: ")
    game1 = float(input("Enter score for game 1: "))
    game2 = float(input("Enter score for game 2: "))
    game3 = float(input("Enter score for game 3: "))
    handicap = float(input("Enter the handicap score: "))

    average_score, average_with_handicap = compute_scores_with_handicap(game1, game2, game3, handicap)
    print(f"Bowler's Last Name: {bowler_last_name}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Average Score with Handicap: {average_with_handicap:.2f}")
    print()

    # Problem 5: Global Variables for Total and Tax
    print("Problem 5: Global Variables for Total and Tax")
    quantity = int(input("Enter quantity of the item: "))
    unit_price = float(input("Enter unit price of the item: "))

    compute_total_and_tax(quantity, unit_price)

    print(f"Total: {total}")
    print(f"Tax: {tax}")

# Run the main function
main()
