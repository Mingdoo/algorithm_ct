function solution(numbers) {
  var answer = [];
  const splitNumbers = numbers.split("");
  for (let i = 0; i <= splitNumbers.length; i++) {
    const res = permutation(splitNumbers, i);
    for (const it of res) {
      answer.push(Number(it.join("")));
    }
  }
  const set = new Set(answer);
  console.log([...set]);
  return [...set].filter((it) => isPrime(it)).length;
}

function permutation(arr, selectNum) {
  let result = [];
  if (selectNum === 1) return arr.map((v) => [v]);

  arr.forEach((v, idx, arr) => {
    const fixer = v;
    const restArr = arr.filter((_, index) => index !== idx);
    const permuationArr = permutation(restArr, selectNum - 1);
    const combineFixer = permuationArr.map((v) => [fixer, ...v]);
    result.push(...combineFixer);
  });
  return result;
}
const isPrime = (num) => {
  for (let i = 2, s = Math.sqrt(num); i <= s; i++)
    if (num % i === 0) return false;
  return num > 1;
};
console.log(solution("011"), "expected: 3");
