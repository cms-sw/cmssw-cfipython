import FWCore.ParameterSet.Config as cms

def CandSelector(**kwargs):
  mod = cms.EDFilter('CandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
