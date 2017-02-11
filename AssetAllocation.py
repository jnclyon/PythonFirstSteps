# A simple Asset Allocation tool for individuals
# Builds an allocation between stocks, bonds, and gold based on risk
# tolerance and ability to take risk.

def get_asset_allocation(bond_values):

    total_assets = float( input("How much money do you have in liquid assets? ") )
    how_old = float( input("How old are you? ") )
    tolerance = str.capitalize( 
        input("Is your risk tolerance Conservative, Moderate, or Aggressive? ")
    )
    how_much = float( input("How much money do you spend per month? ") )
    
    percent_withdraw = how_much * 12 / total_assets * 100
    
    
    high = bond_values[-1]
    middle = bond_values[1]
    low = bond_values[0]
    
    if how_old > 70:
        bonds_age = high
    elif how_old <= 70 and how_old >= 50:
        bonds_age = middle
    elif how_old < 50:
        bonds_age = low
    
    if tolerance == "Conservative":
        bonds_tol = high
    elif tolerance == "Moderate":
        bonds_tol = middle
    elif tolerance == "Aggressive":
        bonds_tol = low
                
    if percent_withdraw > 5:
        bonds_draw = high
    elif percent_withdraw <= 5 and percent_withdraw >= 4:
        bonds_draw = middle
    elif percent_withdraw < 4:
        bonds_draw = low
        
    my_bond_total = float((bonds_draw + bonds_tol + bonds_age)/3)          
    my_stock_total = float((100 - my_bond_total)*.8)                
    my_gold_total = float((100 - my_bond_total)*.2)
    
    
    print(
        '''
        You have $%s in liquid assets to invest with us.
        You are %d years old.
        You want a portfolio that is %s.
        You want to spend $%s per month.
        This means your allocation should be:
            %.1f%% in Stocks
            %.1f%% in Gold
            %.1f%% in Bonds
        ''' % (
                format(total_assets,",.0f"), how_old, tolerance,
                format(how_much,",.0f"),
                my_stock_total, my_gold_total, my_bond_total
                )
    )

get_asset_allocation( (20, 30, 40) )