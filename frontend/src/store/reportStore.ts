import { create } from "zustand";

export interface Recommendation {
  category: string;
  priority: "high" | "medium" | "low";
  title: string;
  description: string;
}

export interface Report {
  overall_score: number;
  seo_score: number;
  ux_score: number;
  copy_score: number;
  performance_score: number;
  conversion_score: number;

  summary: string;

  recommendations: Recommendation[];
}

interface ReportStore {
  url: string;
  report: Report | null;

  storeUrl: (url: string) => void;
  setReport: (report: Report) => void;
  clearReport: () => void;
}

export const useReportStore = create<ReportStore>((set) => ({
  url: "",
  report: null,

  storeUrl: (url) => set({ url }),

  setReport: (report) => set({ report }),

  clearReport: () =>
    set({
      url: "",
      report: null,
    }),
}));