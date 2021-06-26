import React from 'react';
import './App.css';
import Menu from './tutorial/components/Menu';
import Nav from './tutorial/components/Nav';
import Products from './tutorial/Products';
import {BrowserRouter, Route} from 'react-router-dom'
import Main from './main/Main';
import ProductsCreate from './tutorial/ProductsCreate';
import ProductsEdit from './tutorial/ProductsEdit';

function App() {
  return (
    <div className="App">
    
     
          <BrowserRouter>
          <Route path = '/' exact component={Main}/>
          <Route path = '/admin/products' exact component = {Products}/>
          <Route path = '/admin/products/create' exact component = {ProductsCreate}/>
          <Route path = '/admin/products/:id/edit' exact component = {ProductsEdit}/>
          </BrowserRouter>
     
    
    </div>
  );
}

export default App;
