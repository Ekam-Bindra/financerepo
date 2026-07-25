import type { Metadata } from "next";
import "geist/font/mono";
import "geist/font/sans";

import "./globals.css";

export const metadata: Metadata = {
  title: "Equity Research Assistant",
  description:
    "A source-grounded workspace for public-company financial research.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
