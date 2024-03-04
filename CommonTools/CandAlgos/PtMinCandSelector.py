import FWCore.ParameterSet.Config as cms

def PtMinCandSelector(**kwargs):
  mod = cms.EDFilter('PtMinCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
