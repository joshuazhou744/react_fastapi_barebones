import { React, useState, useEffect} from 'react'
import axios from 'axios'


function Form() {

    const [content, setContent] = useState('')
    const [title, setTitle] = useState('')
    const [grade, setGrade] = useState("")

    const addPostHandler = () => {
        axios.post(`${process.env.API_URL}/climbs`, {"title" : title, "content": content, "grade": grade})
        .then(res => console.log(res))
    }

  return (
    <div>
        <h1>Add Posts</h1>
        <span className="card">
            <input className='titleIn' placeholder='Title' onChange={event => {
                setTitle(event.target.value)
            }}/>
            <input className='contentIn' placeholder='Content' onChange={event => {
                setContent(event.target.value)
            }}/>
            <input className='gradeIn' placeholder='Grade' onChange={event => {
                setGrade(event.target.value)
            }}/>
            <button className='btn' onClick={addPostHandler}>Add Post</button>
        </span>
    </div>
  )
}

export default Form
