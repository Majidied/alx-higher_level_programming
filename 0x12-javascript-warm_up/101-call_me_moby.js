#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};
