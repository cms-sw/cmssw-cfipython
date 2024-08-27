import FWCore.ParameterSet.Config as cms

def SelectHFMinBias(**kwargs):
  mod = cms.EDFilter('SelectHFMinBias',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
