import React from 'react'
import axios from 'axios'
import './Climb.css'

function Climb({climb, url}) {
    const deleteClimbHandler = (title) => {
        axios.delete(`${url}/climbs/${title}`)
            .then(res => console.log(res.data))
    }

  return (
    <div>
        <p key={climb.id}>
            <span>{climb.title}: </span> {climb.content} {climb.grade}
            <button className="button"onClick={() => deleteClimbHandler(climb.title)}>Delete Post</button>
        </p>
    </div>
  )
}

export default Climb
