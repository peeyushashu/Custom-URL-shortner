import Axios from "axios";
import React, { Component } from "react";
import "semantic-ui-css/semantic.min.css";
import { Button, Container, Form, TextArea, Divider } from 'semantic-ui-react'


class App extends Component {
  state = { 
    longurl:"",
    loading: false,
    error: null,
    data: null
 }

 handleGetShortURL= () =>{
  this.setState({loading: true})
  Axios.post('http://127.0.0.1:8000/add-url/', {url:this.state.longurl})
    .then(res=>{
        this.setState({data: res.data , loading:false})
    })
    .catch(err=>{
        this.setState({error: err, loading:false})
    })
}

  handleChange = e => {
    this.setState({ longurl : e.target.value });
  };
 
  render() {
    const {data, error, loading, longurl}= this.state;
    return (
      <Container>
        <Form>
          <Form.Input label='URL' placeholder='Enter Long URL' onChange={this.handleChange} value={longurl} />
          <Button onClick={this.handleGetShortURL}>Submit</Button>
        </Form>
        <Divider/>
        {error ? <p>{this.error}</p>:data ? <>
            <h2>Short URL is:</h2>
            <a href={data && data.data.ShortURL}>{data && data.data.ShortURL}</a>
        </>: <></>}
      </Container>
    );
  }
}

export default App;



