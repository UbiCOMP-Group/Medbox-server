export const API_URL =
    process.env.NODE_ENV === "development"
        ? "http://localhost:8000/api"
        : "production_url_not_defined";
