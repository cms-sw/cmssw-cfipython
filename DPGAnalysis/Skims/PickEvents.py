import FWCore.ParameterSet.Config as cms

def PickEvents(**kwargs):
  mod = cms.EDFilter('PickEvents',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
