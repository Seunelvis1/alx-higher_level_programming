#!/usr/bin/node
export const callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
export default callMeMoby;
