const solution = (a, b) => {
  return a.map(($, _) => a[_] * b[_]).reduce((a, b) => a + b, 0);
};

console.log(solution([1, 2, 3, 4], [-3, -1, 0, 2]));
