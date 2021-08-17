const node=(
  key=null,nxt=null
  ) => ({
  "key":key,
  "nxt":nxt
});

//insert front
const shift= (h,e)=> node(
  e,h
);

//remove front
const dequeue= h=> [
  h.key,
  h.nxt? h.nxt: node()
];

//insert rear
const append= (h,e)=>(
  h.nxt?
    node(
      h.key,
      append(h.nxt,e))
  :h.key?
    node(h.key,node(e))
  :node(e)
);
const visible= e=>(
  parseFloat(e)? true
  : e!==0?visible(
      Object.keys(e).length)
  :false
);
const err= msg=> console.error(
   "!!!ERROR: "
   +msg
);
//pop from linkedStack
const pop= (h,t=node())=>(
  !h.key? 
    err('Empty List')
  :h.nxt?
    pop(h.nxt,
    append(t,h.key))
  :[h.key, t]
);
  

//test
const l = [1,2,3].reduce(
  (a,e)=>append(a,e),
  node()
);
console.log(pop(l),pop(node()));
console.log(append(l, 6));


const contains= (
  h,k,f=(e,r)=>e===r)=> (
    !f(h.key,k)?
      h.nxt?
        contains(h.nxt,k,f)
      :false
    :h.key
);

/*export {
  node as list,append,
  dequeue,pop,peekInto
};*/