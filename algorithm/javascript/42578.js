function solution(clothes) {
  var answer = 1;
  const map = new Map();
  for (const [name, category] of clothes) {
    map.set(category, (map.get(category) || 0) + 1);
  }

  for (const [_, num] of map) {
    answer *= num + 1;
  }

  if (answer === 1) {
    return 0;
  }
  return answer - 1;
}

console.log(
  solution([
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
  ]),
);
