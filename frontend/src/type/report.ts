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