import * as funclib from './functools.js';
import * as graphlib from './graph.js';
import * as listlib from './linkedlist.js';

console.log(funclib.I("root"));
//--------------------
const prb = [
  'a=b$1','b=f$1','a=c$9','b=d$1','a=e$5',
  'c=e$2','d=e$1','c=d$3','b=e$2','f=d$6'
];

const parseCost= info=> info.split("$").slice(-1).pop();
const parseEdge= info=> info.split("$")[0].split("=");

const makeEdge= info=>[...parseEdge(info),parseCost(info)];

const graph = prb.reduce(
    (a,e)=>graphlib.updateGraph(a,makeEdge(e)),
    {...graphlib.Graph()}
);
/////////////////////////
const ll = listlib;
const dta = ll.list();

console.log(
  dta,
  ll.append(dta,5),
  ll.append(dta,7),
  ll.append(dta,6),
  ll.dequeue(dta),
  ll.dequeue(dta),
  //append(dta,23),
  //peekInto({"compare":(a,b)=>a===b},dta,23),
);
console.log(
  graph,
  //getNeighboursOf('e', graph),
  //getUniqueNodes([[1,2,3]], 2)
  //getId(graph, 'b')
);

document.querySelector
('body').innerHTML=[
  ...graph.vertex
];
