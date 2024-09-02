import React from 'react'
import Climb from './Climb'

function Posts({climbs, url}) {
  return (
    <div>
        <h1>Posts</h1>
      <ul>
        {climbs.map(climb => <Climb climb={climb} url={url}/>)}
      </ul>
    </div>
  )
}

export default Posts
