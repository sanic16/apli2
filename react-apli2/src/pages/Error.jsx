import React from "react";
import NavBar from "../components/NavBar";

const ErrorPage = () => {
  return (
    <>
      <NavBar />
      <main>
        <h1>Error!</h1>
        <p>
          La página que está solicitando no existe o no se encuentra disponible
          en este momento
        </p>
      </main>
    </>
  );
};

export default ErrorPage;
