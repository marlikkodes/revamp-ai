import { api } from "./api";

export async function analyzeWebsite(url: string) {
  const response = await api.post("/analyze", {
    url,
  });

  return response.data;
 
}