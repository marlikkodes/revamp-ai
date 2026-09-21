import { ArrowRight} from "lucide-react";

interface Recommendation {
  category: string;
  priority: "high" | "medium" | "low";
  title: string;
  description: string;
}

interface RecommendationCardProps {
  recommendation: Recommendation;
}

export default function RecommendationCard({
  recommendation,
}: RecommendationCardProps) {
  const priorityStyles = {
    high: {
      bg: "bg-red-100",
      text: "text-red-700",
      label: "High Priority",
    },

    medium: {
      bg: "bg-yellow-100",
      text: "text-yellow-700",
      label: "Medium Priority",
    },

    low: {
      bg: "bg-green-100",
      text: "text-green-700",
      label: "Low Priority",
    },
  };

  const style = priorityStyles[recommendation.priority];

  return (
    <div className="rounded-3xl border border-border bg-card p-7 shadow-sm transition hover:-translate-y-1 hover:shadow-lg">

      <div className="flex items-center justify-between">

        <span className="text-sm font-semibold uppercase text-primary">
          {recommendation.category}
        </span>

        <span
          className={`rounded-full px-3 py-1 text-xs font-semibold ${style.bg} ${style.text}`}
        >
          {style.label}
        </span>

      </div>

      <h3 className="mt-5 text-xl font-bold text-text-main">
        {recommendation.title}
      </h3>

      <p className="mt-4 leading-7 text-text-secondary">
        {recommendation.description}
      </p>

      <button className="mt-6 flex items-center gap-2 text-primary font-medium hover:gap-3 transition-all">
        View Details

        <ArrowRight size={18} />
      </button>

    </div>
  );
}