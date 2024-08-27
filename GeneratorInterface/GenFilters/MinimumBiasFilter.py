import FWCore.ParameterSet.Config as cms

def MinimumBiasFilter(**kwargs):
  mod = cms.EDFilter('MinimumBiasFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
