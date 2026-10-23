import FWCore.ParameterSet.Config as cms

def NMaxPerLumi(*args, **kwargs):
  mod = cms.EDFilter('NMaxPerLumi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
