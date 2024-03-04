import FWCore.ParameterSet.Config as cms

def L1DEFilter(**kwargs):
  mod = cms.EDFilter('L1DEFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
