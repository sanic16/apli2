import React from 'react'
import { FaTimes, FaCheck} from 'react-icons/fa'

const PriceCard = props => {
  return (
    <div className='flow-root w-[18.75rem] 
    bg-gradient-to-b from-black/80 to-black/100  bg-cover text-white text-center rounded-lg shadow-2xl shadow-black/60
    duration-300 hover:scale-105 m-12 lg:m-0 lg:m-4'>
        <div className='mb-10'>
            <h3 className='text-xl font-semibold text-violet-500 m-8
            border-0 border-solid border-b-[1px] border-white p-[10px]'>
                {props.data.service}
            </h3>
            <h1 className='text-6xl'><sup className='text-3xl'>$</sup>{props.data.price}</h1>
        </div>
        <div className='mb-16'>
            <ul>
                <li className='m-4'><FaCheck className={props.data.item1 ? `text-green-400 inline mr-6` : `text-red-400 inline mr-6`}/>Almacenamiento Básico</li>
                <li className='m-4'><FaTimes className={props.data.item2 ? `text-green-400 inline mr-6` : `text-red-400 inline mr-6`}/>Componentes Avanzados</li>
                <li className='m-4'><FaTimes className={props.data.item3 ? `text-green-400 inline mr-6` : `text-red-400 inline mr-6`}/>Métricas</li>
                <li className='m-4'><FaCheck className={props.data.item4 ? `text-green-400 inline mr-6` : `text-red-400 inline mr-6`}/>Componentes Básicos</li>
                <li className='m-4'><FaTimes className={props.data.item5 ? `text-green-400 inline mr-6` : `text-red-400 inline mr-6`}/>SSL</li>
                <li className='m-4'><FaTimes className={props.data.item6 ? `text-green-400 inline mr-6` : `text-red-400 inline mr-6`}/>Aplicación Móvil</li>
            </ul>
        </div>
        <div className='mb-10'>
            <button type='button' className='w-30 px-4 py-2 bg-violet-600 text-gray-300 font-semibold
            rounded-full cursor-pointer uppercase'>Suscribirse</button>
        </div>
    </div>
  )
}

export default PriceCard