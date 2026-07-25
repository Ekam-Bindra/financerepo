import type { HealthResponse } from "@equity-research/api-contracts";
import { NextResponse } from "next/server";

export const dynamic = "force-dynamic";

export function GET() {
  const response: HealthResponse = {
    service: "web",
    status: "ok",
    version: process.env.APP_VERSION ?? "0.1.0",
    timestamp: new Date().toISOString(),
  };

  return NextResponse.json(response, {
    headers: {
      "Cache-Control": "no-store",
    },
  });
}
