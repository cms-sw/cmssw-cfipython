import FWCore.ParameterSet.Config as cms

def TestSeedingLayers(*args, **kwargs):
  mod = cms.EDAnalyzer('TestSeedingLayers',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
