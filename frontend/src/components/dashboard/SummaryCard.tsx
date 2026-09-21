import { Sparkles } from "lucide-react";

interface SummaryCardProps {
  summary: string;
}

export default function SummaryCard({ summary }: SummaryCardProps) {
  return (
    <section className="rounded-3xl border border-border bg-card p-8 shadow-sm">
      <div className="mb-6 flex items-center gap-4">
        <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-primary/10">
          <Sparkles className="h-6 w-6 text-primary" />
        </div>

        <div>
          <h2 className="text-2xl font-bold text-text-main">
            AI Executive Summary
          </h2>

          <p className="text-sm text-text-secondary">
            An overview of your website's strengths and biggest opportunities.
          </p>
        </div>
      </div>

      <div className="rounded-2xl bg-background p-6">
        <p className="leading-8 text-[17px] text-text-secondary">
          {summary}
        </p>
      </div>
    </section>
  );
}