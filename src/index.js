import './index.css';

import React from 'react';
import ReactDOM from 'react-dom';

import App from './App';
import MyFirst from './MyFirst'
import * as serviceWorker from './serviceWorker';


function MySecond() {
  return (
      <ul><li>1 < /li>
      <li>2</li > </ul>)
}

ReactDOM.render(<MyFirst />,
      document.getElementById('root'))
  ReactDOM.render(<MySecond />, document.getElementById('not_root'))


  console.dir(document);
  console.log(document.domain)