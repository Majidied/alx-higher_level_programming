#!/usr/bin/node

let nbPr = 0;
exports.logMe = function (item) {
  console.log(nbPr + ': ' + item);
  nbPr++;
};
