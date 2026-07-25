export type ServiceStatus = "ok" | "degraded";

export interface HealthResponse {
  service: "web" | "api";
  status: ServiceStatus;
  version: string;
  timestamp: string;
}

export interface DependencyHealth {
  status: "ok" | "unavailable";
  latencyMs?: number;
  error?: string;
}

export interface ReadinessResponse extends HealthResponse {
  dependencies: {
    postgres: DependencyHealth;
    redis: DependencyHealth;
  };
}
