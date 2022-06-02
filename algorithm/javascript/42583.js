function solution(bridge_length, weight, truck_weights) {
  var answer = 0;
  let currentWeight = 0,
    time = 0,
    q = [[0, 0]];
  on = 0;
  while (truck_weights.length > 0 || q.length > 0) {
    if (q[0][1] === time) {
      currentWeight -= q.shift()[0];
    }
    if (currentWeight + truck_weights[0] <= weight && on + 1 <= bridge_length) {
      currentWeight += truck_weights[0];
      q.push([truck_weights.shift(), time + bridge_length]);
    }
    time++;
  }
  return time;
}

console.log(solution(2, 10, [7, 4, 5, 6]));
