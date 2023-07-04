datas = []
while True:
    name = input('ชื่อ-สกุล: ')
    student_id = input('รหัสนักศึกษา: ')
    score1 = float(input('คะแนนเก็บ: '))
    score2 = float(input('คะแนนสอบกลางภาค: '))
    score3 = float(input('คะแนนสอบปลายภาค: '))

    total_score = (score1 * 0.3) + (score2 * 0.3) + (score3 * 0.4)
    grade = 'A' if total_score >= 80 else 'B' if total_score >= 70 else 'C' if total_score >= 60 else 'D' if total_score >= 50 else 'F'

    datas.append({
        'name': name,
        'student_id': student_id,
        'score1': score1,
        'score2': score2,
        'score3': score3,
        'total_score': total_score,
        'grade': grade,
    })

    if input('พิมพ์ X เพื่อยกเลิก: ') == 'x':
        break

for data in datas:
    print('---------------------------------')
    print('ชื่อ-สกุล: {}'.format(data['name']))
    print('รหัสนักศึกษา: {}'.format(data['student_id']))
    print('คะแนนเก็บ: {}'.format(data['score1']))
    print('คะแนนสอบกลางภาค: {}'.format(data['score2']))
    print('คะแนนสอบปลายภาค: {}'.format(data['score3']))
    print('คะแนนรวม: {}'.format(data['total_score']))
    print('เกรด: {}'.format(data['grade']))
    print('---------------------------------')

total_score = sum(data['total_score'] for data in datas)
average = total_score / len(datas)
max_score = max(data['total_score'] for data in datas)
min_score = min(data['total_score'] for data in datas)

grade_counts = {grade: sum(1 for data in datas if data['grade'] == grade) for grade in ['A', 'B', 'C', 'D', 'F']}

print('คะแนนเฉลี่ย: {}'.format(average))
print('คะแนนสูงสุด: {}'.format(max_score))
print('คะแนนต่ำสุด: {}'.format(min_score))
print('จำนวนคนที่ได้เกรด A: {}'.format(grade_counts['A']))
print('จำนวนคนที่ได้เกรด B: {}'.format(grade_counts['B']))
print('จำนวนคนที่ได้เกรด C: {}'.format(grade_counts['C']))
print('จำนวนคนที่ได้เกรด D: {}'.format(grade_counts['D']))
print('จำนวนคนที่ได้เกรด F: {}'.format(grade_counts['F']))
