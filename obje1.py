class Tax:
    def __init__(self, income, insurance):
        self.income = income
        self.insurance = insurance

    def calculate_tax(self):
        return self.income * 0.3 - self.insurance

    def display(self):
        result = self.get_net_income()
        print('ชื่อ : ', userName)
        print('รายได้ : ', self.income)
        print('เงินประกันชีวิต : ', self.insurance)
        print('เงินลดหย่อนค่าใช้จ่าย : ', result['expense'])
        print('เงินลดหย่อนประกันชีวิต : ', result['net_insurance'])
        print('เงินลดหย่อนส่วนตัว : ', result['private_discount'])
        print('อัตราภาษี : ', result['vat_rate'])
        print('ภาษีที่ต้องชำระ : ', result['vat'])
        print('รายได้สุทธิ : ', result['net_income'])
        print('รายได้สุทธิหลังหักภาษี : ', result['net_income_after_tax'])

    def get_vat_rate(self):
        income = self.income
        if income <= 50000:
            return 0
        elif income <= 100000:
            return 0.05
        elif income <= 500000:
            return 0.1
        elif income <= 1000000:
            return 0.2
        elif income <= 4000000:
            return 0.3
        else:
            return 0.37

    def get_expense(self):
        expense = self.income * 0.4
        if expense > 60000:
            return 60000
        elif expense < 0:
            return 0
        else:
            return expense

    def get_insurance(self):
        insurance = self.insurance
        if insurance > 50000:
            return 50000
        elif insurance < 0:
            return 0
        else:
            return insurance

    def get_net_income(self):
        income = self.income
        expense = self.get_expense()
        private_discount = 30000
        income_with_dc = income - expense - private_discount if income - \
            expense - private_discount > 0 else 0
        net_insurance = self.get_insurance()
        net_income = income_with_dc - \
            net_insurance if income_with_dc - net_insurance > 0 else 0
        vat_rate = self.get_vat_rate()
        vat = vat_rate * net_income
        net_income_after_tax = income - vat if income - vat > 0 else 0
        return {
            'private_discount': private_discount,
            'net_income': net_income,
            'net_income_after_tax': net_income_after_tax,
            'net_insurance': net_insurance,
            'expense': expense,
            'vat_rate': vat_rate,
            'vat': vat,
        }


# if main
if __name__ == '__main__':
    datas = []
    while True:
        userName = input('กรุณาระบุชื่อ : ')
        income = int(input('กรุณาระบุรายได้ : '))
        insurance = int(input('กรุณาระบุเงินประกันชีวิต: '))
        datas.append(Tax(income, insurance))
        if input('พิมพ์ X เพื่อยกเลิกและคำนวณภาษี: ') == 'x':
            break

    # create loop for display value from user input
    for data in datas:
        print('------------------')
        data.display()
        print('------------------')
