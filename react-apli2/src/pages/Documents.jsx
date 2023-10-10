import React from "react";
import arquitectura from "../assets/images/arquitectura.png";

const DocumentsPage = () => {
  return (
    <>
      <h1 className="text-center my-8 text-4xl text-violet-900">
        Arquitectura
      </h1>

      <div className="mx-auto w-[90%] md:w-[70%] my-10">
        <img className="mx-auto" src={arquitectura} alt="" />
      </div>
    </>
  );
};

export default DocumentsPage;
