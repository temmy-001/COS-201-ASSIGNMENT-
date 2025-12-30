def calculate_tax(filing_status, taxable_income):
    """
    Calculate US federal income tax for 2009 based on filing status and taxable income.
    
    Parameters:
    filing_status (int): 0=Single, 1=Married Jointly, 2=Married Separately, 3=Head of Household
    taxable_income (float): The taxable income amount
    
    Returns:
    float: Total tax amount
    """
    
    # Define tax brackets for each filing status (2009 rates)
    # Each bracket is defined as: [upper_limit, rate]
    # The last bracket has upper_limit as None (meaning infinity)
    
    brackets = {
        # Single
        0: [
            (8350, 0.10),
            (33950, 0.15),
            (82250, 0.25),
            (171550, 0.28),
            (372950, 0.33),
            (None, 0.35)  # None means no upper limit (infinity)
        ],
        # Married Filing Jointly
        1: [
            (16700, 0.10),
            (67900, 0.15),
            (137050, 0.25),
            (208850, 0.28),
            (372950, 0.33),
            (None, 0.35)
        ],
        # Married Filing Separately
        2: [
            (8350, 0.10),
            (33950, 0.15),
            (68525, 0.25),
            (104425, 0.28),
            (186475, 0.33),
            (None, 0.35)
        ],
        # Head of Household
        3: [
            (11950, 0.10),
            (45500, 0.15),
            (117450, 0.25),
            (190200, 0.28),
            (372950, 0.33),
            (None, 0.35)
        ]
    }
    
    # Get the appropriate brackets for the filing status
    tax_brackets = brackets[filing_status]
    
    tax = 0.0
    previous_limit = 0  # Track the lower bound of the current bracket
    
    # Calculate tax using progressive system
    for upper_limit, rate in tax_brackets:
        if taxable_income <= previous_limit:
            break  # Income is already fully taxed
            
        if upper_limit is None or taxable_income <= upper_limit:
            # This is the last bracket the income falls into
            taxable_amount = taxable_income - previous_limit
            tax += taxable_amount * rate
            break
        else:
            # Income exceeds this bracket, tax the entire bracket amount
            taxable_amount = upper_limit - previous_limit
            tax += taxable_amount * rate
            previous_limit = upper_limit
    
    return tax


def main():
    """Main function to interact with user and calculate tax."""
    
    # Display instructions
    print("=== US Federal Income Tax Calculator (2009) ===")
    print("Filing Status Options:")
    print("  0 - Single")
    print("  1 - Married Filing Jointly or Qualified Widow(er)")
    print("  2 - Married Filing Separately")
    print("  3 - Head of Household")
    print()
    
    # Get user input with validation
    while True:
        try:
            status = int(input("Enter filing status (0-3): "))
            if status not in [0, 1, 2, 3]:
                print("Error: Please enter a number between 0 and 3.")
                continue
            
            income = float(input("Enter taxable income: $"))
            if income < 0:
                print("Error: Income cannot be negative.")
                continue
                
            break  # Valid input received
            
        except ValueError:
            print("Error: Please enter valid numbers.")
    
    # Calculate tax
    tax_amount = calculate_tax(status, income)
    
    # Display results
    print("\n" + "="*50)
    print(f"Filing Status: ", end="")
    status_names = ["Single", "Married Filing Jointly", "Married Filing Separately", "Head of Household"]
    print(status_names[status])
    print(f"Taxable Income: ${income:,.2f}")
    print(f"Total Tax: ${tax_amount:,.2f}")
    print("="*50)
    
    # Show example calculation breakdown for educational purposes
    if income <= 100000:  # Only show breakdown for reasonable incomes
        print("\nTax Breakdown (approximate):")
        print("This shows how different portions of your income are taxed at different rates.")
        
        # Simple breakdown
        brackets = {
            0: [(8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (None, 0.35)],
            1: [(16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (None, 0.35)],
            2: [(8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (None, 0.35)],
            3: [(11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (None, 0.35)]
        }
        
        tax_brackets = brackets[status]
        remaining_income = income
        previous_limit = 0
        
        for i, (upper_limit, rate) in enumerate(tax_brackets):
            if remaining_income <= 0:
                break
                
            if upper_limit is None:
                bracket_amount = remaining_income
            else:
                bracket_amount = min(remaining_income, upper_limit - previous_limit)
            
            if bracket_amount > 0:
                bracket_tax = bracket_amount * rate
                print(f"  ${previous_limit:,.2f} - ${previous_limit + bracket_amount:,.2f}: {rate*100:.0f}% = ${bracket_tax:,.2f}")
                previous_limit += bracket_amount
                remaining_income -= bracket_amount


# Run the program
if __name__ == "__main__":
    main()