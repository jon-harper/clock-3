---
title: Bill of Materials Introduction
summary: An introduction to reading the Clock 3 Bill of Materials.
authors: Jon Harper
date: 2022-04-05
---

*This document is actively being refined and edited for mistaeks.*
## Overview

We designed Clock 3 with several rules related to sourcing and parts in mind:

- Every new line added to the BOM has an up front cost.
- Rare parts are expensive and hard to find, by definition.
- Standardized and *de facto* standard parts are cheaper and have more suppliers.
- Custom fabricated anything is expensive.

With those rules in mind, we aim to both keep costs down and make sourcing parts as simple as possible.

## Keeping Track

Every component that goes in to making a Clock 3 printer is assigned an ID number and categorized in several ways.
 
- Is it a printed part or something purchased?
- Does it require modification or assembly, such as finished cables or insulation cut to size?
- Is it an aid for assembly or maintence that isn't part of the printer itself?
- Finally, what is the general function of the part in the printer (e.g. frame, electronics, motion)?

## Categorization

Let's talk about identifying the things you'll need to print, buy, or make. Parts are given a number with a two letter prefix and a three-digit number code, for example `PN001`.

### Prefixes

`MN`: Parts in the format `MN###` are raw materials. During the assembly process, they'll be modified or used to make something else. Typically this can't be reversed: examples are connector pins and heat shrink tubing. This list is not exhaustive--if you won't need to buy or assemble it, it's not given a number. For example, you probably won't cut the frame extrusions yourself, so we don't include the raw aluminum in the list.

`UN`: These parts aren't actually part of the printer but you will need them to put it together or keep it running. You may already have some or all of these on hand, like a soldering iron or set of Metric hex wrenches.

`PN`: These are finished parts, whether printed, purchased, or made from materials. They come in the format `PN###`.

!!! note
    If the number after `PN` is less than 399, it's a printed part.

### Fabricated parts

There are several kinds of these:

- Printed parts, with or without heat set inserts
- Cables and wiring harnesses
- Cut extrusions and panels

With the exception of cables, all of these have part numbers in the form `PN`. Cables *do* still have an ID, but are tracked based on the component that they power. There's more on that later in the assembly guide.

All of these fabricated parts require materials (`MN`). Consequently, some parts in the BOM are made entirely from materials.