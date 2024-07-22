import FWCore.ParameterSet.Config as cms

def NMaxPerLumi(**kwargs):
  mod = cms.EDFilter('NMaxPerLumi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod