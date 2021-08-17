// utils low level
const __isMin=(key,ref)=>key<ref;

const __isEqual=(key,ref)=>key===ref;

const __swapArrayItems=(arr,key,ref)=>(
  [...arr].map(
    _=> __isEqual(_,arr[key])? arr[ref]
      :__isEqual(_,arr[ref])? arr[key]:_)
);

const isEmpty=itr=>(
  typeof(itr)==="object"?
    !Object.keys(itr).length
  :!itr.length
);

//selection Sort
function _selectionScan(cfg,arr,key,ref){
  const newArr= (
    cfg.compare(arr[ref],arr[key])?
      cfg.swap(arr,key,ref)
    :[...arr]
  );return(
    newArr.length===ref? newArr
    :_selectionScan(cfg,newArr,key,ref+1)
  );
}

function selectionSort(cfg,arr,key=0){
  if (key===arr.length) return arr;
  const scannedArr=cfg.modifier(arr,key,key+1);
  return selectionSort(cfg,scannedArr,key+1);
}

//Quick Sort
function _partition(cfg,arr){
  const pivot = arr[arr.length-1];
  const left=[],right=[];
  arr.map(
    x=>cfg.compare(x,pivot)?
      left.push(x)
    :right.push(x)
  );
  return [left.slice(),pivot,right.slice(0,-1)];
}

function quickSort(cfg, arr){
  if (arr.length<2) return [...arr];
  const [left,pivot,right]=cfg.modifier(arr);
  return ([
    ...quickSort(cfg,left),
    pivot,
    ...quickSort(cfg,right)
  ]);
}


//******************************************\\
//sample test data
const data = {
  "avg":[4,6,3,1,2,7,8,5],
  "worst":[8,7,6,5,4,3,2,1],
  "best":[1,2,3,4,5,6,7,8]
};
//selection sort test
const selCfg = {
  "modifier": makeCurry(_selectionScan,2,{
    'swap':__swapArrayItems,
    'compare':__isMin
  })
};
const selSorted = makeCurry(selectionSort,2,selCfg);
console.log(selSorted(data.worst));

//quickSort test
const qckCfg = {
  "modifier": makeCurry(_partition,2,{
    "compare":__isMin
  })
};
const qckSorted= makeCurry(quickSort,2,qckCfg);
console.log(qckSorted(data.avg));
