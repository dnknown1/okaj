/*eVerThIng is function
(*!^) atlest true or false.
*****************************
*L* Lambda function signature.
*****************************
*f* Atomic function element.
 * as f() reduces to eVeryThIng
*****************************
*Lf.f* Function expansion.
 * as @(f) reduces to f
*****************************
*g: Lf.f* Functon reference
 * as g reduces to @f.f
*****************************
*Lfgh.fgh* Function compose
 * as Lfgh reduces to (f(g))(h)
*/
//** Unary Combinators
//@f.f: Identity 
const I = f=> f;
//@f.ff: Mockingbird/or* 
const M = f=> f(f);

//** Binary Combinators
//@fg.f: Kestral/True
const K = f=> g=> f;
//@fg.g: Kite: false
const KI= f=> g=> g;
//** ternary Combinators
//Lfgh.f(g)(h): Cardinal/negetion
const C = f=> g=> h=> f(h)(g);
//Lfgh.f(gh): Bluebird/compose
const B = f=> g=> h=> f(g(h));

/*Logical Combinators*/
//Cardinal/negetion
const not = C;
//Lpq.ppq: Disjunction/or
const or  = p=> q=> M(p)(q);
//Lpq.pqp: Conjunction/and
const and = p=> q=> p(q)(p);
//Lpq.pq(C(q)): Boolean Equality
const bEq = p=> q=> p(q)(C(q));

//**utilities
//Lf.f(true)(false) converts to javascript Boolean
const truth=f=>f(true)(false);
const makeCurry = (f,n,..._)=>(
  _.length<n?(...__)=>
    makeCurry(f,n,..._,...__)
  :f(..._)
);
//exports 
export {
  I,M,K,KI,C,B,
  not,or,and,bEq,
  makeCurry
};