import { Button } from "@/components/ui/button";
import { Download, Share2, Globe } from "lucide-react";

interface ReportHeaderProps {
  url: string;
}

export default function ReportHeader({ url }: ReportHeaderProps) {

  const current_time = new Date().toLocaleString();

  return (
    <header className="flex items-start justify-between">

      <div>

        <h1 className="text-5xl font-bold text-text-main">
          Website Report
        </h1>

        <div className="mt-6 flex items-center gap-4 rounded-2xl border border-border bg-card p-5 shadow-sm">

          <div className="rounded-full bg-primary/10 p-3">
            <Globe className="text-primary" />
          </div>

          <div>

            <h2 className="font-semibold text-lg">
              {url}
            </h2>

            <p className="text-sm text-text-secondary">
              Analyzed {current_time}
            </p>

          </div>

        </div>

      </div>

      <div className="flex gap-4">

        <Button variant="outline" className="h-12 rounded-xl">
          <Download className="mr-2 h-4 w-4" />
          Download PDF
        </Button>

        <Button className="h-12 rounded-xl">
          <Share2 className="mr-2 h-4 w-4" />
          Share Report
        </Button>

      </div>

    </header>
  );
}