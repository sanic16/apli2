import React from "react";
import PriceCard from "../components/PriceCard";
import { motion } from "framer-motion";

const services = [
  { id: 1, service: "Free", price: 0, item1: true, item2: true, item3: false, item4: false, item5: false, item6: false},
  { id: 2, service: "Standard", price: 16, item1: true, item2: true, item3: true, item4: true, item5: true, item6: false},
  { id: 3, service: "Premium", price: 40, item1: true, item2: true, item3: true, item4: true, item5: true, item6: true},
];

const ProductsPage = () => {
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
    }}>
      <h1 className="text-center my-8 text-4xl text-violet-900">Nuestros Servicios</h1>

      <div className="w-[90%] flex justify-around flex-wrap  mx-auto my-8">
        {services.map(service => (
          <PriceCard key={service.id} data={service} />
        )
        )}
      </div>
    </motion.div>
  );
};

export default ProductsPage;
