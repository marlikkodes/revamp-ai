import UrlForm from "../components/landing/UrlForm";



export default function LandingPage() {
  return (
    <section className="relative overflow-hidden bg-background">
      {/* Decorative Background */}
      <div className="absolute left-0 top-0 h-96 w-96 rounded-full bg-primary/10 blur-[140px]" />
      <div className="absolute right-0 bottom-0 h-96 w-96 rounded-full bg-accent/50 blur-[160px]" />

      <div className="relative mx-auto flex min-h-screen max-w-6xl items-center justify-center px-6">
        <div className="w-full max-w-5xl text-center">
          <h1 className="mx-auto max-w-5xl text-6xl font-bold leading-tight tracking-tight text-foreground">
            Find the Highest-Impact Improvements for Your Website
          </h1>

          <p className="mt-8 text-2xl text-muted-foreground">
            Enter your website URL below
          </p>
          

          <div className="mt-14">
            <UrlForm />
          </div>
        </div>
      </div>
    </section>
  );
}