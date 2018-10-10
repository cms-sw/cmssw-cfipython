import FWCore.ParameterSet.Config as cms

SimG4FluxAnalyzer = cms.EDAnalyzer('SimG4FluxAnalyzer',
  LVNames = cms.vstring(
    'TotemT1Part1',
    'TotemT1Part2',
    'TotemT1Part3',
    'TotemT2Part1',
    'TotemT2Part2',
    'TotemT2Part3'
  )
)
