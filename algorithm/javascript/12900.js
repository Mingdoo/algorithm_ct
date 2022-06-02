function solution(n) {
  const dpTable = new Array(n + 1).fill(0);
  dpTable[1] = 1;
  dpTable[2] = 2;
  console.log(dpTable);
  for (let i = 3; i < n + 1; i++) {
    console.log(i / 2, "i / 2");
    const end = i % 2 ? i / 2 : i / 2 + 1;
    for (let j = 1; j < end; j++) {
      console.log(i);
      console.log(dpTable[i - j], dpTable[j], [i - j - 1, j]);
      dpTable[i] += dpTable[i - j] + dpTable[j] - dpTable[j + 1];
    }
  }
  console.log(dpTable);
  // return answer;
}

console.log(solution(4));
