/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
 let answer = [];
let storage = [
15,"FizzBuzz",
3,"Fizz",
5, "Buzz",
];
var counter = 1;
while(counter < n+1) {
answer.push(String(counter));
counter++;
}
for(let i = 0; i < answer.length; i++) {
switch(true) {
case answer[i]%15 == 0:
answer.splice(i,1,"FizzBuzz");
break;
case answer[i]%5 == 0:
answer.splice(i,1,storage[5]);
break;
case answer[i]%3 == 0:
answer.splice(i,1,storage[3]);
break;
}
}
return answer;   
};