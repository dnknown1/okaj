const compare = (x,y,arr)=> arr[x] < arr[y]?x: y;
//***********************\\
//**************************************\\
function compareSwapMutate(mIdx,chqIdx,arr) {//return 1 if swap
  if (chqIdx === compare(mIdx, chqIdx, arr)) {
    swapMutate(mIdx, chqIdx, arr);//side effect
    return 1;//swap
  }//mutation
  return 0;//no swap
}
//****************************\\
function selectionSortMutate(arr) {
  let mIdx=0, count=0, chqIdx=1;//assume min at 0
  const res = [];//comparison count per pass
  while (mIdx<arr.length-1) {
    count += compareSwapMutate(mIdx, chqIdx, arr);
    chqIdx++;
    if (chqIdx === arr.length) {
      chqIdx = ++mIdx+1;
      res.push(count);
      count = 0;
    }//escape logic
  }//compare all
  return res;
}
//const isPassComplete = (mIdx,chqIdx,limit);
//*************************\\
function bubbleSortMutate(arr) {
  let mIdx=0, count=0;
  const res=[];
  const limit=()=> arr.length-res.length-1;

  while (mIdx<limit()) {
    count += compareSwapMutate(mIdx, mIdx+1, arr);
    mIdx++;
    if (mIdx===limit()) {
      res.push(count);
      if (!count) break;
      count=0;
      mIdx=0;
    }// pass complete: exit logic
  }// compare all
  return res;
}
//****************************\\
function insertionSortMutate(arr){
  let p = arr.length-(arr.length-1);
  let mIdx=p,chqIdx=mIdx-1,count=0;
  const res=[];

  while (p<arr.length){
    count = compareSwapMutate(chqIdx, mIdx, arr);//chqIdx to be min
    if (!count||!chqIdx){
      mIdx=++p;//increment pivot
      res.push(count);
    }else{
      mIdx=chqIdx;
      res[res.length-1] += count;
    }
    chqIdx=mIdx-1;
  }
  return res;
}
//**********************************************\\
function binarySearch(key,arr,[s,e]=[0,arr.length]){
  let mid = parseInt((s+e)/2);
  if (arr[mid]===key) return mid;// key found
  if (s===mid) return -1;// base case
  if (key<arr[mid]) return binarySearch(key,arr,[s,mid]);
  if (key>arr[mid]) return binarySearch(key,arr,[mid,e]);
}
 //***** :TESTING: ****\\
//**********************\\
/*/:-----> Tests
let testData = getTestData();
console.log(testData,testSort(testData,selectionSortMutate));

testData = getTestData();
console.log(testData,testSort(testData,bubbleSortMutate));

testData = getTestData();
console.log(testData,testSort(testData,insertionSortMutate));
/*/
/*
01234
43215 : m1c0->swap
34215 : m2c1->swap
32415 : m1c0->swap
23415 : m3c2->swap
23145 : m2c1->swap
21345 : m1c0->swap
12345 : m4c3->nswp
end
*/
function selectionSort(arr,compfunc=compareSwapCount,
state={"key":0,"next":1,"swaps":[0]}) {
  const s= [...state.swaps];
  if(state.key===arr.length-1) return s; //baseCase
  
  const {key:k,next:n}=state;
  const isPassDone= n===arr.length;
  s[s.length-1]+= compfunc(state,arr);//updateSwap
  const newState= {
    "key" : isPassDone?k+1:k,
    "next": isPassDone?k+2:n+1,
    "swaps":isPassDone?[...s,0]:[...s]};
  return selectionSort(arr,compfunc,newState);
}
//const selectionSort;
//console.log(
//  testData.worst,
//  selectionSort(testData.worst),
//);

const compareMin=(key,...r)=> (
  r.length? key<r[0]
  :nxt=> compareMin(key, nxt)
);//compareSwap
const swapMutate=(arr,...r)=> (
  r.length<2? (...rest)=> swapMutate(arr,...r,...rest)
  :arr[r[0]]=arr.splice(r[1],1,arr[r[0]])[0]
);//missing next arr any
const getTestData=()=>({
  "avg":[4,6,3,1,2,7,8,5],
  "worst":[8,7,6,5,4,3,2,1],
  "best":[1,2,3,4,5,6,7,8]
});//sample test data
// module
function compareSwapCount({key:k,next:n},arr){
    if(!compareMin(arr[k],arr[n])){
      swapMutate(arr,k,n);
      return 1;}
    return 0;
}
function testSort(func,...args) {
  const res = {"funcName": func.name, "stats": {}};
  for (const key in args[0]) {
    res.stats[key] = {
      "data": [...args[0][key]],
      "counts": func(args[0][key],...args.slice(1))
    };//test result
  }return res;}
//sorting


const testData = getTestData();
console.log(
testData.worst,
swapMutate(testData.worst,0,7),
swapMutate(testData.worst)(1,6),
swapMutate(testData.worst)(2)(5),
compareMin(testData.worst[3],testData.worst[4]),
compareMin(testData.worst[0])(testData.worst[1]),
compareSwapCount({"key":3,"next":4}, testData.worst),
testData.avg,
selectionSort(testData.avg)
);