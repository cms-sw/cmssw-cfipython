import FWCore.ParameterSet.Config as cms

def MCZll(**kwargs):
  mod = cms.EDFilter('MCZll',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
