
trades=[200,-500,5600,100,1000,990,100,3000,900,-2000,-149,-14551]
print('Total p/l',sum(trades))
print('biggest lose',min(trades))
print('biggest win',max(trades))

def average_win(trades):
    profit_trades=[]
    for x in trades:
        if x>0:
            profit_trades.append(x)
    return sum(profit_trades)/len(profit_trades)       

def win_rate(trades):
    winrate=0
    for x in trades:
        if x>0:
            winrate=winrate+1
    return (winrate/len(trades))*100

avg=average_win(trades)
print('average_win',avg)

win=win_rate(trades)
print('win rate',win)




            
            


    

    
    




        



