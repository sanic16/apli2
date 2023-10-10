import React from "react";
import { Outlet } from "react-router-dom";
import NavBar from "../components/NavBar";
import Footer from "../components/Footer";
import { AnimatePresence } from "framer-motion";

const RootLayout = () => {
  return (
    <>
      <NavBar />
      <main className="min-h-[calc(100vh-128px)]">
        <AnimatePresence 
        mode="wait"
        >
          <Outlet />
        </AnimatePresence>
      </main>
      <Footer />
    </>
  );
};

export default RootLayout;
