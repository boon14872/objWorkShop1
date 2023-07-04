
datas = []
while True:
    userName = input('กรุณาระบุชื่อ : ')
    income = int(input('กรุณาระบุรายได้ : '))
    insurance = int(input('กรุณาระบุเงินประกันชีวิต: '))
    expense = income * 0.4
    expense = 60000 if expense > 60000 else expense if expense >= 0 else 0
    net_insurance = 50000 if insurance > 50000 else insurance if insurance >= 0 else 0
    private_discount = 30000
    income_with_dc = income - expense - private_discount
    net_income = income_with_dc - net_insurance
    vat_rate = 0
    if net_income <= 50000:
        vat_rate = 0
    elif net_income <= 100000:
        vat_rate = 0.05
    elif net_income <= 500000:
        vat_rate = 0.1
    elif net_income <= 1000000:
        vat_rate = 0.2
    elif net_income <= 4000000:
        vat_rate = 0.3
    else:
        vat_rate = 0.37


    vat = vat_rate * net_income
    net_income_after_tax = income - vat
    data = {
        'userName': userName,
        'income': income,
        'insurance': insurance,
        'net_income': net_income,
        'net_income_after_tax': net_income_after_tax,
        'vat': vat,
        'vat_rate': vat_rate,
        'net_insurance': net_insurance,
        'expense': expense,
        'private_discount': private_discount,
    }
    datas.append(data)
    if input('พิมพ์ X เพื่อยกเลิกและคำนวณภาษี: ').lower() == 'x':
        break

for data in datas:
    print('------------------')
    print('ชื่อ :', data['userName'])
    print('รายได้ :', data['income'])
    print('เงินประกันชีวิต :', data['insurance'])
    print('รายได้สุทธิ :', data['net_income'])
    print('รายได้สุทธิหลังหักภาษี :', data['net_income_after_tax'])
    print('ภาษีที่ต้องชำระ :', data['vat'])
    print('อัตราภาษี :', data['vat_rate'])
    print('เงินประกันชีวิตสุทธิ :', data['net_insurance'])
    print('ค่าใช้จ่าย :', data['expense'])
    print('ส่วนลดส่วนตัว :', data['private_discount'])
    print('------------------')
