import React from 'react'

const Button = (props) => {
  return (
    <button onClick={props.onClick} className={props.className + ' rounded-full px-12 py-2 text-white'}>
        {props.children}
    </button>
  )
}

export default Button