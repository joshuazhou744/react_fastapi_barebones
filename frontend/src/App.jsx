import { useState, useEffect } from 'react'
import Form from './Form'
import axios from 'axios'
import Posts from './Posts'


function App() {

  const [posts, setPosts] = useState([{}])

    useEffect(() => {
        axios.get('http://localhost:8000/climbs')
        .then(res => {
            setPosts(res.data)
        })
    })

  return (
    <div>
      <Form />
      <Posts climbs={posts}/>
    </div>
  )
}

export default App
