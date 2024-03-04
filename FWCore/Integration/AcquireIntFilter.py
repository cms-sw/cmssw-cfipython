import FWCore.ParameterSet.Config as cms

def AcquireIntFilter(**kwargs):
  mod = cms.EDFilter('AcquireIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
