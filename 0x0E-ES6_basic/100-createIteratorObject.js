export default function createIteratorObject(report) {
  const employees = [];
  for (const item of Object.values(report.allEmployees)) {
    employees.push(...item);
  }
  return employees;
}
