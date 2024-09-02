import { useState, useEffect } from 'react'
import Form from './Form'
import axios from 'axios'
import Posts from './Posts'

function App() {

  const [posts, setPosts] = useState([{}])
  console.log(process.env.API_URL)

    useEffect(() => {
        axios.get(`${process.env.API_URL}/climbs`)
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
