"use client";

import { useState } from "react";

import RecommendationCard from "./ReccomendationCard";

interface Recommendation {
  category: string;
  priority: "high" | "medium" | "low";
  title: string;
  description: string;
}

interface Props {
  recommendations: Recommendation[];
}

export default function RecommendationSection({
  recommendations,
}: Props) {
  const [filter, setFilter] = useState("all");

  console.log("Recommendations:", recommendations);

  const filtered =
    filter === "all"
      ? recommendations
      : recommendations.filter(
          (r) => r.priority === filter
        );

  return (
    <section className="space-y-8">

      <div className="flex items-center justify-between">

        <h2 className="text-3xl font-bold text-text-main">
          Recommendations
        </h2>

        <div className="flex gap-3">

          {["all", "high", "medium", "low"].map((level) => (

            <button
              key={level}
              onClick={() => setFilter(level)}
              className={`rounded-full px-5 py-2 capitalize transition

              ${
                filter === level
                  ? "bg-primary text-white"
                  : "bg-card border border-border text-text-secondary"
              }
              `}
            >
              {level}
            </button>

          ))}

        </div>

      </div>

      <div className="grid gap-6 lg:grid-cols-2">

        {filtered.map((recommendation, index) => (

          <RecommendationCard
            key={index}
            recommendation={recommendation}
          />

        ))}

      </div>

    </section>
  );
}