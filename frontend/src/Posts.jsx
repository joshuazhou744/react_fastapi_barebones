import React from 'react'
import Climb from './Climb'

function Posts({climbs}) {
  return (
    <div>
        <h1>Posts</h1>
      <ul>
        {climbs.map(climb => <Climb climb={climb} />)}
      </ul>
    </div>
  )
}

export default Posts
