import React from "react";
import iot1 from "../assets/images/iot1.jpg";
import { motion } from "framer-motion";

const AboutPage = () => {
  return (
    <motion.div
      initial={{
        opacity: 0,
        y: -100,
      }}
      animate={{
        opacity: 1,
        y: 0,
      }}
      exit={{
        opacity: 0,
        y: -100,
      }}
      open
      transition={{
        ease: "linear", duration: .4
      }}
    >
      <header>
        <h2
          className="text-center text-violet-900
        text-4xl my-8"
        >
          Acerca de GridTech
        </h2>
      </header>
      <div className="w-[90vw] mx-auto my-12 grid grid-cols-1 lg:grid-cols-2 gap-x-10 gap-y-16">
        <article>
          <section>
            <h2 className="mx-auto max-w-[50rem] mb-6 capitalize font-bold text-violet-900 text-2xl">
              Nuestros dispositivos para un mundo conectado
            </h2>
            <p className="mb-6 max-w-[50rem] mx-auto">
              Bienvenido a <span>GridTech</span>, su socio en la construcción de
              un mundo más inteligente y conectado. Nos especializamos en
              diseñar y fabricar dispositivos inteligentes de última generación
              para hogares e industrias, todos impulsados por la versátil
              plataforma ESP8266
            </p>
            <section>
              <h2 className="mx-auto max-w-[50rem] mb-6 capitalize font-bold text-violet-900 text-2xl">
                Llevando la innovación a tu hogar
              </h2>
              <p className="mb-6 max-w-[50rem] mx-auto">
                En nuestra misión de hacer la vida cotidiana más cómoda y
                eficiente, ofrecemos una gama de soluciones para el hogar
                inteligente. Desde iluminación inteligente y control climático
                hasta seguridad y entretenimiento, nuestros dispositivos basados
                en ESP8266 están diseñados para integrarse perfectamente en su
                hogar, mejorando su comodidad y tranquilidad.
              </p>
            </section>
            <section>
              <h2 className="mx-auto max-w-[50rem] mb-6 capitalize font-bold text-violet-900 text-2xl">
                Empoderar a las industrias con IoT
              </h2>
              <p className="mb-6 max-w-[50rem] mx-auto">
                GridTech no se limita sólo a los hogares inteligentes. Estamos
                dedicados a transformando industrias a través del Internet de
                las Cosas (IoT). Nuestras soluciones de ESP8266 de grado
                industrial permiten a las empresas optimizar procesos, reducir
                los costos operativos y mejorar la productividad en todos
                diversos sectores.
              </p>
            </section>
          </section>
        </article>
        <div className="max-w-[50rem] mx-auto my-auto">
          <img className="rounded-2xl" src={iot1} alt="" />
        </div>
      </div>
    </motion.div>
  );
};

export default AboutPage;
