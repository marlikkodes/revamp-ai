import ScoreCard from "./ScoreCard";

import {
  TrendingUp,
  Search,
  Pencil,
  Gauge,
  Target,
  Monitor,
} from "lucide-react";

interface Props {
  report: {
    overall_score: number;
    seo_score: number;
    ux_score: number;
    copy_score: number;
    performance_score: number;
    conversion_score: number;
  };
}
export default function ScoreSection({ report }: Props) {
    
  return (
    <section className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-3">

      <ScoreCard
        title="Overall Score"
        score={report.overall_score}
        Icon={TrendingUp}
      />

      <ScoreCard
        title="SEO Score"
        score={report.seo_score}
        Icon={Search}
      />

      <ScoreCard
        title="UX Score"
        score={report.ux_score}
        Icon={Monitor}
      />

      <ScoreCard
        title="Copy Score"
        score={report.copy_score}
        Icon={Pencil}
      />

      <ScoreCard
        title="Performance Score"
        score={report.performance_score}
        Icon={Gauge}
      />

      <ScoreCard
        title="Conversion Score"
        score={report.conversion_score}
        Icon={Target}
      />

    </section>
  );
}