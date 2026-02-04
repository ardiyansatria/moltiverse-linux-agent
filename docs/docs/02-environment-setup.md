# Environment Setup

This document describes the Linux environment setup used for this project.

The agent is developed and executed in a minimal Linux environment running on Android using Termux.

---

## Device and OS

- Device: Android smartphone
- OS: Android
- Linux Environment: Termux

---

## Termux Installation

Termux is installed from F-Droid to ensure up-to-date packages.

Steps:
1. Install F-Droid
2. Install Termux from F-Droid
3. Launch Termux

---

## Base Package Setup

After launching Termux, the following packages are installed:

```bash
pkg update && pkg upgrade
pkg install git python nodejs
