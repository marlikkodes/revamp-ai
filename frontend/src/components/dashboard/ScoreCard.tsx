import { LucideIcon } from "lucide-react";

interface ScoreCardProps {
  title: string;
  score: number;
  Icon: LucideIcon;
}

export default function ScoreCard({
  title,
  score,
  Icon,
}: ScoreCardProps) {
  const getStatus = (score: number) => {
    if (score < 70) {
      return {
        label: "Needs Work",
        color: "text-red-600",
      };
    }

    if (score < 90) {
      return {
        label: "Good",
        color: "text-yellow-600",
      };
    }

    return {
      label: "Great",
      color: "text-green-600",
    };
  };

  const status = getStatus(score);

  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-sm transition hover:shadow-md">
      <div className="mb-5 flex items-center justify-between">
        <div className="rounded-xl bg-primary/10 p-3">
          <Icon className="h-6 w-6 text-primary" />
        </div>

        <span className={`text-sm font-semibold ${status.color}`}>
          {status.label}
        </span>
      </div>

      <h3 className="text-sm font-medium text-text-secondary">
        {title}
      </h3>

      <p className="mt-2 text-4xl font-bold text-text-main">
        {score}
      </p>
    </div>
  );
}