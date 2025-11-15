#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$Command,
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Args
)
switch ($Command) {
    "spec:validate" {
        & python -m spoon_diversity.cli validate @Args
    }
    "spec:sync" {
        & python -m spoon_diversity.cli sync @Args
    }
    "spec:derive" {
        if ($Args -contains "--all") {
            & bash ./scripts/kiro spec:derive --all
        } else {
            throw "Usage: scripts/kiro.ps1 spec:derive --all"
        }
    }
    default {
        throw "Unknown command: $Command"
    }
}

