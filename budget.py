class Category:

    def __init__(self, name): 
        self.name = name
        self.ledger = list()
        self.balance = 0
        self.withdraw_amount = 0

    def deposit(self, amount, description = ''):
        self.balance = self.balance + amount
        self.description = description
        d = {'amount': amount, 'description': self.description}
        self.ledger.append(d)

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount) != True:
            return False
        self.description = description
        withdraw_amount = amount * -1
        d = {'amount': withdraw_amount, 'description': self.description}
        self.ledger.append(d)
        self.balance = self.balance + withdraw_amount
        self.withdraw_amount = withdraw_amount + self.withdraw_amount
        return True

    def get_balance(self):
        return(self.balance)

    def transfer(self, amount, category):
        if self.check_funds(amount) == False:
            return(False)
        else:
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return(True)

    def check_funds(self, amount):
        if amount > self.balance:
            return(False)
        else:
            return(True)

    def __str__(self):
        string = self.name
        new_string = string.center(30, '*')
        newlst = list()
        total = 0
        for item in self.ledger:
            amt = item['amount']
            total = amt + total
            amt = str(amt)
            if '.' not in amt:
                amt = str(amt) + '.00'
            else:
                amt = str(format(float(amt), '.2f'))
            des = item['description']
            if len(des) > 23:
                des = des[0:23]
            newlst.append(des + amt.rjust(30-len(des)))
        total = str(format(float(total), '.2f')) 
        if len(newlst) == 1:
            return (new_string + '\n' + newlst[0] + '\n' + 'Total: ' + total)
        if len(newlst) == 2:
            return (new_string + '\n' + newlst[0] + '\n' + newlst[1] + '\n' + 'Total: ' + total)
        if len(newlst) == 3:
            return (new_string + '\n' + newlst[0] + '\n' + newlst[1] + '\n' + newlst[2] + '\n' + 'Total: ' + total)
        if len(newlst) == 4:
            return (new_string + '\n' + newlst[0] + '\n' + newlst[1] + '\n' + newlst[2] + '\n' + newlst[3] + '\n' + 'Total: ' + total)

def create_spend_chart(categories):
    ans = []
    title = 'Percentage spent by category'
    ans.append(title)
    y_axis = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']
    percentagelist = []
    numlist = []
    bars = []
    totalwithdraws = 0
    for i in categories:
        totalwithdraws = i.withdraw_amount + totalwithdraws
    for i in categories:
        totalpercategory = int((abs(i.withdraw_amount) / abs(totalwithdraws))* 100)
        if totalpercategory < 10:
            totalpercategory = 0
        totalpercategory = str(totalpercategory)
        try:
            if totalpercategory[1] != '0':
                totalpercategory = int(totalpercategory[0] + '0')
        except:
            pass
        percentagelist.append(totalpercategory)
    for i in percentagelist:
        num = round(int(i) / 10)
        numlist.append(num)
    print(numlist)

    strlen = 3

    for i in range(100, -10, -10):
        if len(str(i)) < strlen:
            diff = strlen - len(str(i))
            line = diff * ' ' + str(i) + '| '
        else:
            line = str(i) + '| '
        for item in percentagelist:
            percent = int(item)
            if i <= percent:
                line = line + 'o' + '  '
            else:
                line = line + ' '*3
        ans.append(line)

    if len(percentagelist) == 1:
        dash = '    ----'
        ans.append(dash)
    if len(percentagelist) == 2:
        dash = '    -------'
        ans.append(dash)
    if len(percentagelist) == 3:
        dash = '    ----------'
        ans.append(dash)
    else:
        dash = '    -------------'
        ans.append(dash)

    maxlength = 0
    verticalprint = []
    for i in categories:
        words = i.name
        verticalprint.append(words)
        if len(words) > maxlength:
            maxlength = len(words)
    for n, j in enumerate(verticalprint):
        if len(j) < maxlength:
            addspace = maxlength - len(j)
            j = j + ' ' * addspace
            verticalprint[n] = j

    for x, y, z in zip(*verticalprint): 
        x_axis = x.rjust(6) + y.rjust(3) + z.rjust(3) + '  '
        ans.append(x_axis)
        

    finalsolution = ''
    for i in ans:
        finalsolution = finalsolution + '\n' + i
    finalsolution = finalsolution.lstrip()
    print(finalsolution)
    return(finalsolution)