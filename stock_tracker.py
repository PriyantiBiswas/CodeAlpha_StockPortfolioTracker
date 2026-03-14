import os

def main():
    
    stock_prices = {
        "AAPL": 180.0,
        "TSLA": 250.0,
        "GOOGL": 140.0,
        "MSFT": 400.0,
        "AMZN": 170.0
    }

    portfolio = {}
    
    print(" Welcome to the Stock Portfolio Tracker ")
    print("Available stocks and their current prices:")
    for ticker, price in stock_prices.items():
        print(f"  {ticker}: ${price:.2f}")
    print(" ")
    
    
    while True:
        ticker = input("\nEnter stock ticker (or type 'done' to finish): ").strip().upper()
        if ticker == 'DONE':
            break
        
        if ticker not in stock_prices:
            print("Error: Stock not found in our database. Please select from the available stocks.")
            continue
            
        try:
            quantity_str = input(f"Enter quantity of shares for {ticker}: ").strip()
            quantity = float(quantity_str)
            if quantity < 0:
                print("Error: Quantity cannot be negative.")
                continue
            
            
            if ticker in portfolio:
                portfolio[ticker] += quantity
            else:
                portfolio[ticker] = quantity
        except ValueError:
            print("Error: Invalid input. Please enter a valid number for the quantity.")
            
    
    print("      PORTFOLIO SUMMARY       ")
    
    
    total_investment = 0.0
    summary_lines = [
        
        "      PORTFOLIO SUMMARY       "
        
    ]
    
    if not portfolio:
        print("No stocks added to the portfolio.")
        summary_lines.append("No stocks added to the portfolio.")
    else:
        for ticker, qty in portfolio.items():
            value = qty * stock_prices[ticker]
            total_investment += value
            line = f"{ticker:5s} | {qty:8.2f} shares @ ${stock_prices[ticker]:6.2f} = ${value:10.2f}"
            print(line)
            summary_lines.append(line)
            
    total_line = f"\nTOTAL INVESTMENT VALUE: ${total_investment:,.2f}"
    print(total_line)
    summary_lines.append(total_line)
    
    
    save_option = input("Would you like to save this summary to a file? (y/n): ").strip().lower()
    
    if save_option == 'y':
        filename = input("Enter filename (e.g., portfolio.txt): ").strip()
        if not filename:
            filename = "portfolio.txt"
        
        try:
            with open(filename, 'w') as f:
                f.write("\n".join(summary_lines))
            print(f"Success! Portfolio summary has been saved to '{filename}'.")
        except IOError as e:
            print(f"Failed to save the file: {e}")

if __name__ == "__main__":
    main()
    