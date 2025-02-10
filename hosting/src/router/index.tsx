import { Route, Routes } from "react-router-dom";
import { Home } from "../pages";
import { BaseLayout } from "../components";

export const Router = () => {
  return (
    <Routes>
      <Route path="*" element="Error 404" />
      <Route
        path="/"
        element={
          <BaseLayout>
            <Home />
          </BaseLayout>
        }
      />
    </Routes>
  );
};
