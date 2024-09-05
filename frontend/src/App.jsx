import { useState, useEffect } from 'react'
import Form from './Form'
import axios from 'axios'
import Posts from './Posts'

const VITE_API_URL = import.meta.env.VITE_API_URL
console.log(VITE_API_URL)

function App() {

  const [posts, setPosts] = useState([{}])

    useEffect(() => {
        axios.get(`${VITE_API_URL}/climbs`)
        .then(res => {
            setPosts(res.data)
        })
    })

  return (
    <div>
      <Form url={VITE_API_URL}/>
      <Posts climbs={posts} url={VITE_API_URL}/>
    </div>
  )
}

export default App
