import FWCore.ParameterSet.Config as cms

def GlobalTightHalo2016Filter(**kwargs):
  mod = cms.EDFilter('GlobalTightHalo2016Filter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
