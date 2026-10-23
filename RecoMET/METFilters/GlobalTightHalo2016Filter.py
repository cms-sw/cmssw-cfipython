import FWCore.ParameterSet.Config as cms

def GlobalTightHalo2016Filter(*args, **kwargs):
  mod = cms.EDFilter('GlobalTightHalo2016Filter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
