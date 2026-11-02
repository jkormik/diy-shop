---
name: Handmade Soul
description: A sanctuary for unique, slow-crafted handmade embroidery and decor.
colors:
  primary: "#1C1917"
  neutral-bg: "#F9F7F2"
  surface-low: "#F5F5F4"
  surface-mid: "#E7E5E4"
  surface-high: "#D6D3D1"
  text-main: "#4A4A4A"
  text-muted: "#78716C"
typography:
  display:
    fontFamily: "Georgia, serif"
    fontSize: "3.75rem"
    fontWeight: 700
    lineHeight: 1.2
  body:
    fontFamily: "Georgia, serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  sm: "8px"
  md: "12px"
  lg: "24px"
  full: "9999px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "32px"
  xl: "64px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#FFFFFF"
    rounded: "{rounded.full}"
    padding: "16px 32px"
  button-secondary:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.text-main}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
---

# Design System: Handmade Soul

## Overview

**Creative North Star: "The Soulful Sanctuary"**

Handmade Soul is a digital extension of a physical sanctuary. The aesthetic is refined and quiet, designed to evoke the feeling of a cozy room filled with sunlight and the scent of linen. It rejects the urgency of modern e-commerce in favor of a "slow-craft" rhythm, where breathing room (white space) is as important as the content itself.

The visual language balances the soft, tactile nature of embroidery with a grounded, strong foundation that reflects the passion of its creator.

**Key Characteristics:**
- **Organic Geometry**: Heavy use of rounded corners and circular motifs to remove industrial hardness.
- **Quiet Palette**: A tonal range of stone and beige that allows the colorful products to be the primary focus.
- **Rhythmic Spacing**: Generous margins and padding that encourage slow browsing.

## Colors

A muted, earthy palette that provides a neutral backdrop for colorful handmade textiles.

### Primary
- **Deep Charcoal Slate** (#1C1917): Used for primary actions, strong headlines, and grounding elements. It represents the "inner fire" and strength of the creator.

### Neutral
- **Cream Linen** (#F9F7F2): The primary background. Evokes natural fabrics and warmth.
- **Soft Pebble** (#F5F5F4): Section backgrounds and subtle fills.
- **Warm Grey** (#E7E5E4): Borders, dividers, and inactive states.
- **Stone Dust** (#D6D3D1): Mid-tone accents and secondary surface elements.
- **Earth Charcoal** (#4A4A4A): Main body text; softer than pure black for better readability on cream.
- **Muted Slate** (#78716C): Secondary text, labels, and subtle captions.

**The Rare Accent Rule.** The primary Deep Charcoal Slate is used purposefully for focus. It should never overwhelm the "quiet" nature of the site.

## Typography

**Display Font:** Georgia (with serif fallbacks)
**Body Font:** Georgia (with serif fallbacks)

**Character:** A timeless, editorial pairing that suggests craftsmanship, tradition, and a personal touch.

### Hierarchy
- **Display** (Bold, 60px, 1.2): Hero headlines; used to set the emotional tone of a page.
- **Headline** (Bold, 30px, 1.3): Section titles; clear and authoritative but not aggressive.
- **Title** (Medium, 20px, 1.4): Product names and sub-headings.
- **Body** (Regular, 18px, 1.6): Product descriptions and long-form copy. Optimized for a relaxed reading pace.
- **Label** (Medium, 14px, 1.2): Navigation, buttons, and meta-data.

## Layout

The layout follows a "breathable" grid. Containers are wide (`max-w-7xl`) with substantial internal padding. Responsive transitions are fluid, moving from a spacious desktop experience to a focused, single-column mobile view that preserves the "sanctuary" feel.

## Elevation & Depth

The system utilizes **Soft Depth**. Rather than harsh, structural shadows, it uses diffuse, ambient glows and tonal layering to create a tactile feel.

### Shadow Vocabulary
- **Ambient Glow** (`box-shadow: 0 4px 20px rgba(0,0,0,0.05)`): Used for cards and floating elements to make them feel like they are resting lightly on the surface.
- **Tactile Lift** (`box-shadow: 0 10px 30px rgba(0,0,0,0.08)`): Used for primary buttons and active elements on hover to simulate a physical press.

## Shapes

The form language is strictly organic. Sharp corners are forbidden.
- **Full Rounds**: All primary buttons and interactive pills use `rounded-full`.
- **Soft Edges**: Cards and image containers use `rounded-3xl` or `rounded-xl` to evoke the softness of fabric.

## Components

### Buttons
- **Shape**: Full pill (`rounded-full`)
- **Primary**: Deep Charcoal Slate background with White text. High contrast for clear action.
- **Hover / Focus**: Soft lift with a slight darkening of the background.
- **Secondary**: Soft Pebble background with Earth Charcoal text; subtle and non-intrusive.

### Cards / Containers
- **Corner Style**: Generous rounding (`rounded-2xl` to `rounded-3xl`).
- **Background**: Cream Linen or White.
- **Shadow Strategy**: Ambient Glow to create a soft separation from the background.
- **Internal Padding**: Large (`px-6 py-8`) to maintain the quiet aesthetic.

### Navigation
- **Style**: Minimalist, sticky top bar.
- **States**: Soft color shift (Stone-800 $\to$ Green-700) to indicate activity without breaking the palette.

## Do's and Don'ts

### Do:
- **Do** use generous white space to avoid a "cluttered" shop feel.
- **Do** prioritize Georgia serif for all expressive text to maintain the artisanal identity.
- **Do** use organic shapes (full rounds) for all interactive elements.

### Don't:
- **Don't** use pure black (#000) or pure white (#FFF) for large surfaces; stay within the stone/cream palette.
- **Don't** use sharp corners or 90-degree angles on any UI element.
- **Don't** use aggressive, high-saturation colors that clash with the "quiet" sanctuary mood.
