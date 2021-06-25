import React from 'react';
import './App.css';
import Menu from './tutorial/components/Menu';
import Nav from './tutorial/components/Nav';
import Products from './tutorial/Products';
import {BrowserRouter, Route} from 'react-router-dom'
import Main from './main/Main';

function App() {
  return (
    <div className="App">
    
     
          <BrowserRouter>
          <Route path = '/' exact component={Main}/>
          <Route path = '/admin/products' component = {Products}/>
          </BrowserRouter>
     
    
    </div>
  );
}

export default App;
