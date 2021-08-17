class App extends React.Component{
    constructor(props){
        super(props);
        this.state = {nEmp: 0, qty: [], dsbd:true};
    }
    handleChange = (e)=>{
        this.setState({nEmp:e.target.value, dsbd: false});
    }
    
    render(){return (React.createElement("div",{id:"id_app_rnd"},
        React.createElement("label",{htmlFor:"io_nEmp"},"Oh! Hello, how many employees?"),
        React.createElement("br",null),
        React.createElement("input",{
            id:"io_nEmp",
            type:"Number",
            placeholder:0,
            autofocus:true,
            onChange: this.handleChange}),
        React.createElement("input",{id:"btn_nEmp",
                type: "submit",
                onClick: (e)=> this.setState({qty: [...this.state.qty, new Array(this.state.nEmp)]}),
                disabled: !this.state.nEmp}),
        this.state.nEmp), //end div
        console.log(this.state.qty)
    )}
}