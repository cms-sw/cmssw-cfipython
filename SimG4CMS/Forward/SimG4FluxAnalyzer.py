import FWCore.ParameterSet.Config as cms

def SimG4FluxAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SimG4FluxAnalyzer',
    LVNames = cms.vstring(
      'TotemT1Part1',
      'TotemT1Part2',
      'TotemT1Part3',
      'TotemT2Part1',
      'TotemT2Part2',
      'TotemT2Part3'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
