#!/usr/bin/node

exports.esrever = function (list) {
  const ReversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    ReversedList.push(list[i]);
  }
  return ReversedList;
};
