import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Switch, Route } from 'react-router-dom'

import './styles/main.scss'

import Home from './components/pages/Home'

const App = () => {
  return (
    <>
      <BrowserRouter><Switch>
        <Route exact path='/' component={Home} />
      </Switch>
      </BrowserRouter>
    </>
  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
