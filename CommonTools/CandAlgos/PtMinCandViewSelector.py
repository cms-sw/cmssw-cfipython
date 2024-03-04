import FWCore.ParameterSet.Config as cms

def PtMinCandViewSelector(**kwargs):
  mod = cms.EDFilter('PtMinCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
