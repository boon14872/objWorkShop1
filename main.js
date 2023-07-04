document.addEventListener("DOMContentLoaded", function () {
    let datas = [];
    const addNewSalary = (e) => {
      e.preventDefault();
      const name = document.getElementById("name").value;
      const salary = document.getElementById("salary").value;
      const insurance = document.getElementById("insurance").value;
      const data = {
        name,
        salary: +salary,
        insurance: +insurance,
      };
      let validate = [];
      if (name === "") {
        validate.push(validateInValid("กรุณากรอกชื่อ-นามสกุล", "name"));
      } else {
        validate.push(validateValid("name"));
      }
      if (salary === "") {
        validate.push(validateInValid("กรุณากรอกเงินเดือน", "salary"));
      } else {
        validate.push(validateValid("salary"));
      }

      if (insurance === "") {
        validate.push(
          validateInValid("กรุณากรอกเงินประกันชีวิต", "insurance")
        );
      } else {
        validate.push(validateValid("insurance"));
      }

      if (
        validate.every((v) => {
          return v === true;
        })
      ) {
        datas.push(data);
        document.getElementById("name").value = "";
        document.getElementById("salary").value = "";
        document.getElementById("insurance").value = "";
        console.log(datas);
        document.getElementById("tableBox").innerHTML =
          generateTable(datas);
      } else {
        console.log("กรุณากรอกข้อมูลให้ครบ");
      }
    };
    document
      .getElementById("saveBtn")
      .addEventListener("click", addNewSalary);
    document
      .getElementById("calculateVate")
      .addEventListener("click", (e) => {
        e.preventDefault();
        document.getElementById("tableBox").innerHTML = generateTable(
          datas,
          true
        );
      });
  });

  const getErrorHtml = (error) => {
    let html = `<div class="invalid-feedback d-block" id="error">${error}</div>`;
    return html;
  };

  const validateInValid = (text, field) => {
    document.getElementById(field).classList.add("is-invalid");
    // insert error html after field check error if error is exist
    if (document.getElementById(field).nextElementSibling?.id === "error") {
      document.getElementById(field).nextSibling.remove();
    }
    document
      .getElementById(field)
      .insertAdjacentHTML("afterend", getErrorHtml(text));
    return false;
  };
  const validateValid = (field) => {
    document.getElementById(field).nextSibling?.remove();
    document.getElementById(field).classList?.remove("is-invalid");
    document.getElementById(field).classList.add("is-valid");
    return true;
  };

  const generateTable = (datas, calvat = false) => {
    const incomeData = datas.map((data) => {
      const netIncome = getNetIncome(data.salary, data.insurance);
      return {
        name: data.name,
        salary: data.salary,
        insurance: data.insurance,
        ...netIncome,
      };
    });
    let html = `<table class="table table-bordered w-100">
    <thead>
      <tr>
        <th scope="col">ชื่อ-นามสกุล</th>
        <th scope="col">เงินเดือน</th>
        <th scope="col">เงินประกันชีวิต</th>
        ${
          calvat
            ? `<th scope="col">หักค่าใช้จ่าย</th>
            <th scope="col">ค่าลดหย่อนส่วนตัว</th>
        <th scope="col">ลดหย่อนประกันชีวิต</th>
        <th scope="col">รายได้สุทธิ</th>
        <th scope="col">อัตราภาษีที่ต้องชำระ</th>
        <th scope="col">ภาษีที่ต้องชำระ</th>
        <th scope="col">รายได้หลังหักภาษี</th>`
            : ""
        }
      </tr>
    </thead>
    <tbody>`;
    incomeData.forEach((data) => {
      html += `<tr>
        <td>${data.name}</td>
        <td>${data.salary.toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        })}</td>
        </td>
        <td>${data.insurance.toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        })}</td>
        ${
          calvat
            ? `<td>${data.expense.toLocaleString(undefined, {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2,
              })}</td>
        <td>${data.privateDiscount.toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        })}</td>
        <td>${data.netInsurance.toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        })}</td>
        <td>${data.netIncome.toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        })}</td>
        <td>${data.vatRate}</td>
        <td>${data.vat.toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        })}</td>
        <td>${data.netIncomeAfterTax.toLocaleString(undefined, {
          minimumFractionDigits: 2,
          maximumFractionDigits: 2,
        })}</td>`
            : ""
        }
      </tr>`;
    });
    html += `</tbody>
    </table>`;
    return html;
  };
  const getNetIncome = (income, insurance) => {
    console.log(income, insurance);
    const expense = getExpense(+income);
    const privateDiscount = 30000;
    const incomeWithDC = +income - expense - privateDiscount;
    const netInsurance = getInsurance(+insurance);
    const netIncome = incomeWithDC - netInsurance;
    const vatRate = calculateVat(netIncome - netInsurance);
    const vat = vatRate * netIncome;
    const netIncomeAfterTax = income - vat;
    return {
      privateDiscount,
      netIncome,
      netIncomeAfterTax,
      netInsurance,
      expense,
      vatRate,
      vat,
    };
  };

  const getExpense = (income) => {
    const expense = income * 0.4;
    if (expense > 60000) {
      return 60000;
    } else if (expense < 0) {
      return 0;
    } else {
      return expense;
    }
  };

  const getInsurance = (insurance) => {
    if (insurance > 50000) {
      return 50000;
    } else if (insurance < 0) {
      return 0;
    } else {
      return insurance;
    }
  };
  const calculateVat = (income) => {
    if (income >= 0 && income <= 50000) {
      return 0;
    } else if (income <= 100000) {
      return 0.05;
    } else if (income <= 500000) {
      return 0.1;
    } else if (income <= 1000000) {
      return 0.2;
    } else if (income <= 4000000) {
      return 0.3;
    } else if (income > 4000000) {
      return 0.37;
    } else {
      return 0;
    }
  };