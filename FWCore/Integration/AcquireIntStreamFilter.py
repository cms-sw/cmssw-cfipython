import FWCore.ParameterSet.Config as cms

def AcquireIntStreamFilter(**kwargs):
  mod = cms.EDFilter('AcquireIntStreamFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
