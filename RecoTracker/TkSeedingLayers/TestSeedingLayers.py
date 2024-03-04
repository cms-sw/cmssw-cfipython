import FWCore.ParameterSet.Config as cms

def TestSeedingLayers(**kwargs):
  mod = cms.EDAnalyzer('TestSeedingLayers',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
