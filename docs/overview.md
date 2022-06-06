---
title: Overview
summary: General overview page for the documentation.
authors: Jon Harper
date: 2022-04-09
---

This site acts as a central documentation point for the Clock 3 project.

## About

For an overview, see the About section pages:

- A list of [features](about/features.md)
- A [gallery](about/gallery.md) of renders and prototype photos
- [Development goals](about/goals.md) for this project
- [Frequently Asked Questions](about/faq.md)

## Status

The Status section contains more details:

- A regularly updated [changelog](status/changelog.md)
- The current and past [releases](status/releases.md)
- The release [roadmap](status/roadmap.md)

## Documentation

In addition, there are help and guides for:

- Sourcing materials
- Fabricating parts
- Assembly (*in progress*)
- Initial configuration (*pending*)

This is a large project with one developer, so this documentation will evolve iteratively and gradually. Feedback is welcome via the [GitHub repository](https://github.com/jon-harper/clock3-docs).

### Bill of Materials

This documentation includes a general [Sales Bill of Materials](/bom/) to guide purchasing and decision making. This is a list of what you will need to actually purchase or have on hand. Some of the materials will need to be modified, fabricated, or permanently used to make other parts before or during assembly. The list of all parts once the raw materials are consumed and ready for assembly is the [Assembly Bill of Materials]().

Think of the Sales BOM as what you need to buy; the Assembly BOM is what you'll use to build.

The Clock 3 repository contains a [more detailed version of these files](https://github.com/jon-harper/clock-3/tree/main/BOM).

### Assembly

We've assembled and then broken down the Clock 3 prototype repeatedly so that you don't have to do the same with yours. Assembly of Clock 3 is meant to be logical, intuitive, and easy: every wire is pre-measured, every heated insert accounted for.

It's a time investment to get everything ready, but the result is a very straightforward assembly process.

### Configuration

Clock 3 runs on [MainsailOS](https://github.com/mainsail-crew/MainsailOS), which is an all-in-one OS for running [Klipper](https://www.klipper3d.org/) firmware with a clean web frontend.

Clock 3 relies on a modified Klipper 12864 menu system and display with more functionality than the stock menu system. 

We've setup several repositories so that you can simply `git clone` the configuration files directly onto your Raspberry Pi in the appropriate directories.
