const getUniqueNodes= (vertex,edge)=>(
  edge.filter(
    v=>!vertex.includes(v)
));

const isSameNode= (key,ref)=>key===ref;

const getNeighboursOf= (node,edges) => (
  edges.filter (
    e=>e.some (
      i=>isSameNode(node,i)//**dependent
)));//**

const Graph =()=>({
  "vertex":[],
  "edge":[],
});


function updateGraph(graph,edge){
  return ({
    "vertex":[...graph.vertex,
      ...getUniqueNodes(graph.vertex,edge.slice(0,2))
    ],
    "edge":isUniqueEdge(graph.edge,edge)?
      [...graph.edge,edge]
    :[...graph.edge]
  });
}

const isUniqueEdge= (edges,edge)=>(
  edges.every(
    e=>e.some(
      c=>!edge.includes(c)
)));

export {
  Graph, updateGraph
};