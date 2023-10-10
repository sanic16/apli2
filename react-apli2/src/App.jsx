import React from "react";
import "@react-pdf-viewer/core/lib/styles/index.css";
import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider} from "react-router-dom";
import HomePage from "./pages/Home";
import AboutPage from "./pages/About";
import RootLayout from "./pages/Root";
import ProductsPage from "./pages/Products";
import DocumentsPage from "./pages/Documents";
import ErrorPage from "./pages/Error";
import { AnimatePresence } from "framer-motion";
import IOTProvider from "./store/IOTProvider";

// const router = createBrowserRouter([
//   {
//     path: "/",
//     element: <RootLayout />,
//     errorElement: <ErrorPage />,
//     children: [
//       { path: "/", element: <HomePage /> },
//       { path: "/about", element: <AboutPage /> },
//       { path: "/products", element: <ProductsPage/>},
//       { path: "/documents", element: <DocumentsPage/>},

//     ],
//   },
// ]);

const routeDefinitions = createRoutesFromElements(
  <Route>
    <Route path="/" element={<RootLayout />}>
      <Route path="/" element={<HomePage />} />
      <Route path="/about" element={<AboutPage />} />
      <Route path="/products" element={<ProductsPage />} />
      <Route path="/documents" element={<DocumentsPage />} />
    </Route>
    <Route path="*" element={<ErrorPage />} />
  </Route>
)

const router = createBrowserRouter(routeDefinitions);

const App = () => {
  return (
    <IOTProvider>
      <RouterProvider router={router} />
    </IOTProvider>
  );
};

export default App;
