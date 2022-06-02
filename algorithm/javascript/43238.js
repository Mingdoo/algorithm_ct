function solution(n, times) {
  let right = Math.max(...times) * n,
    left = 0;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    let possible = 0;
    times.forEach((time) => {
      possible += Math.floor(mid / time);
    });
    if (possible >= n) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return left;
}
console.log(solution(6, [7, 10]));
