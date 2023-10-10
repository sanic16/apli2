import React from 'react'
import { Link, NavLink } from 'react-router-dom'
import {AiOutlineMenu} from 'react-icons/ai'

const NavBar = () => {
  return (
    <header>
    <nav className='flex justify-between items-center h-20 bg-violet-700 px-[3%]
    text-white text-lg'>
        <h1 className='text-xl font-bold'><Link to="/">GridTech Apli2</Link></h1>
        <ul className='hidden gap-4 lg:flex items-center'>
            <li><NavLink className={({isActive})=> (isActive ? 'link-active' : 'link-hover')} to="">Inicio</NavLink></li>
            <li><NavLink className={({isActive})=> (isActive ? 'link-active' : 'link-hover')} to="about">Nosotros</NavLink></li>
            <li><NavLink className={({isActive})=> (isActive ? 'link-active' : 'link-hover')} to="products">Productos</NavLink></li>
            <li><NavLink className={({isActive})=> (isActive ? 'link-active' : 'link-hover')} to="documents">Documentos</NavLink></li>
        </ul> 
        <ul className='flex items-center gap-4'>
            <li className='hidden lg:block px-4 py-1 bg-gray-300 text-violet-900 rounded-sm hover:bg-gray-2http://electronica-aplicada-2.s3-website-us-east-1.amazonaws.com/about00'><Link to="/login">Iniciar Sesión</Link></li>
            <li className='hidden lg:block px-4 py-1 bg-gray-300 text-violet-900 rounded-sm hover:bg-gray-2http://electronica-aplicada-2.s3-website-us-east-1.amazonaws.com/about00'><Link to="/register">Registrarse</Link></li>
            <div className='text-2xl font-bold lg:hidden'><AiOutlineMenu/></div>
        </ul>
        
    </nav>
    </header>
  )
}

export default NavBar