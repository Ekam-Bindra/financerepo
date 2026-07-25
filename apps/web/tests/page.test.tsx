import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import Home from "../src/app/page";

describe("Home", () => {
  it("presents the engineering-foundation status", () => {
    render(<Home />);

    expect(
      screen.getByRole("heading", {
        name: "Evidence-first equity research",
      }),
    ).toBeInTheDocument();
    expect(screen.getByText("Foundation online")).toBeInTheDocument();
    expect(screen.getByText("SEC ingestion")).toBeInTheDocument();
    expect(screen.getAllByText("Not started")).toHaveLength(4);
  });
});
