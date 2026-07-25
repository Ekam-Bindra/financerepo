const foundationCapabilities = [
  {
    label: "Web application",
    detail: "Next.js App Router and TypeScript",
    state: "Ready",
  },
  {
    label: "Backend API",
    detail: "FastAPI with versioned health routes",
    state: "Ready",
  },
  {
    label: "Local data services",
    detail: "PostgreSQL 17 and Redis 7",
    state: "Configured",
  },
  {
    label: "Quality gates",
    detail: "Formatting, lint, types, tests, and build",
    state: "Configured",
  },
];

const futureCapabilities = [
  "SEC ingestion",
  "Document processing",
  "Financial extraction",
  "Research AI",
];

export default function Home() {
  return (
    <main>
      <header className="site-header">
        <a className="wordmark" href="#top" aria-label="Equity Research home">
          <span aria-hidden="true">ER</span>
          Equity Research
        </a>
        <span className="environment">Development foundation</span>
      </header>

      <section className="hero" id="top">
        <div className="eyebrow">
          <span className="status-dot" aria-hidden="true" />
          Foundation online
        </div>
        <h1>Evidence-first equity research</h1>
        <p className="hero-copy">
          The engineering platform is ready for disciplined product development.
          Source-grounded financial workflows will be introduced only after
          their requirements, controls, and validation plans are approved.
        </p>
        <div className="hero-actions">
          <a className="primary-action" href="/api/health">
            View web health
          </a>
          <a
            className="secondary-action"
            href="https://github.com/Ekam-Bindra/financerepo"
          >
            Open repository
          </a>
        </div>
      </section>

      <section className="foundation-section" aria-labelledby="foundation">
        <div className="section-heading">
          <div>
            <p className="section-kicker">PLAT-001</p>
            <h2 id="foundation">Engineering foundation</h2>
          </div>
          <p>Small, testable, and operationally explicit.</p>
        </div>

        <div className="capability-grid">
          {foundationCapabilities.map((capability) => (
            <article className="capability-card" key={capability.label}>
              <div className="card-topline">
                <h3>{capability.label}</h3>
                <span>{capability.state}</span>
              </div>
              <p>{capability.detail}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="boundary" aria-labelledby="delivery-boundary">
        <div>
          <p className="section-kicker">Delivery boundary</p>
          <h2 id="delivery-boundary">Intentionally not implemented</h2>
          <p>
            Product capabilities stay outside this foundation branch. They
            require their own task IDs, evidence contracts, security review, and
            acceptance criteria.
          </p>
        </div>
        <ul>
          {futureCapabilities.map((capability) => (
            <li key={capability}>
              <span>{capability}</span>
              <strong>Not started</strong>
            </li>
          ))}
        </ul>
      </section>
    </main>
  );
}
