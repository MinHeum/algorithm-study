/**
 * @param {number[]} rating
 * @return {number}
 */
var numTeams = function(rating) {
  let i = 0;
  let j = 1;
  let k = 2;
  let answer = 0
  for(i = 0; i < j; i++) {
      for (j = i+1; j < k; j++) {
          for(k = j+1; k < rating.length; k++) {
              if (isValidTeam(rating[i], rating[j], rating[k])) {
                  answer++
              }
          }
      }
  } 
  return answer
};

var isValidTeam = (rateA, rateB, rateC) => {
  if (rateA < rateB && rateB < rateC) {
      return true
  }
  if (rateA > rateB && rateB > rateC) {
      return true
  }
  return false
}