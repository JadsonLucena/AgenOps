# Agents Module

## Purpose

Define formal sub-agents with explicit contracts, stable inputs and outputs, and standardized handoff envelopes.

## What it provides

- one contract per sub-agent
- a shared handoff envelope
- a shared dispatch protocol
- a shared contract template
- a manifest that maps responsibilities to file paths

## Design rule

A role describes responsibility.
A sub-agent contract defines execution boundaries, inputs, outputs, handoff, and stop conditions.

## Shared Task State

Formal sub-agents may coordinate through the shared task state module under `kit/state/`.
