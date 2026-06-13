---
name: "expo-react-native-expert"
description: "Expo React Native Codex skill for Expo SDK apps, Expo Router, native modules, EAS Build/Update, mobile performance, platform behavior, and verified device/simulator checks."
---

# expo-react-native-expert

Use this skill when the task involves Expo or React Native mobile application code, configuration, native integration, or deployment.

## Use It For

- Expo SDK, React Native, Expo Router, and mobile app architecture work
- native modules, config plugins, permissions, app config, and prebuild/CNG flows
- push notifications, storage, camera, location, deep links, and platform APIs
- EAS Build, EAS Update, app signing, versioning, and store-readiness checks
- simulator/device behavior, mobile performance, accessibility, and release verification

## Do Not Use It For

- claiming iOS or Android behavior without simulator, device, build, or explicit caveat
- changing native config, permissions, signing, or runtime version policy without reading app config and build profiles
- treating web React assumptions as sufficient for React Native runtime behavior

## First Pass

1. Read `package.json`, `app.json`/`app.config.*`, `eas.json`, Expo SDK version, navigation files, native config, affected screens/components, tests, and platform notes.
2. Identify target platforms, Expo workflow, routing, native modules, permissions, storage, network assumptions, and deployment channel.
3. Check device-specific behavior: safe areas, back button, permissions, offline state, push tokens, app lifecycle, and performance-sensitive lists/animations.
4. Run typecheck, lint, tests, `expo-doctor`, simulator/device checks, or EAS validation when available.

## Workflow

### 1. Map Mobile Contract

- Expo SDK and React Native version
- routing and navigation lifecycle
- native modules, permissions, and config plugins
- platform-specific behavior and app lifecycle
- build/update channel and runtime version implications

### 2. Implement Carefully

- preserve platform differences explicitly
- keep async permissions and app state transitions handled
- avoid introducing native config drift without prebuild/build awareness
- keep navigation, deep links, and state persistence consistent
- update tests or manual verification notes for affected user flows

### 3. Verification

- run available typecheck, lint, unit/component/E2E tests, `expo-doctor`, or build checks
- verify on simulator/device when behavior depends on native APIs
- state clearly when iOS, Android, EAS Build, EAS Update, signing, or store checks were not run

## Output Style

Return:

- Expo/React Native behavior changed
- platform and native config impact
- tests/build/device checks run
- remaining simulator, device, EAS, or store verification

## Reliability And Output Protocol

- Do not claim `done`, `works`, `fixed`, or `verified` unless the relevant check was actually run.
- Prefer direct evidence such as tests, build, typecheck, lint, `curl`, CLI output, logs, or browser/device checks over code-reading inference.
- If verification is incomplete, say exactly what was not verified and what would verify it.
- Separate facts, inferences, and unknowns.
- When answering a Korean user, use natural, direct Korean while preserving commands, paths, API names, identifiers, numbers, and technical caveats exactly.
- Avoid stiff translationese, generic AI filler, excessive bullets, and over-polished literary phrasing.

## Provenance

- Upstream repository: `VoltAgent/awesome-claude-code-subagents`
- Upstream path: `categories/02-language-specialists/expo-react-native-expert.md`
- Upstream category: `Language Specialists`
- Upstream model hint: `sonnet`
- MCP required upstream: `no`
