import { React, useState} from 'react'

let posts = []

function Form() {

    const [content, setContent] = useState('')
    const [title, setTitle] = useState('')

    const addPost = (e) => {
        e.preventDefault()
        const noteObject = {
            title: title,
            content: content
        }
        posts.push(noteObject)
        console.log(posts)
    }

  return (
    <div>
        <h1>Add Posts</h1>
        <span className="card">
            <input className='titleIn' placeholder='Title' onChange={event => {
                setTitle(event.target.value)
                console.log(title)
            }}/>
            <input className='contentIn' placeholder='Content' onChange={event => {
                setContent(event.target.value)
                console.log(content)
            }}/>
            <button className='btn' onClick={addPost}>Add Post</button>
        </span>

        <h1>Posts</h1>
    </div>
  )
}

export default Form
