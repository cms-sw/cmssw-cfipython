import FWCore.ParameterSet.Config as cms

def GlobalSuperTightHalo2016Filter(*args, **kwargs):
  mod = cms.EDFilter('GlobalSuperTightHalo2016Filter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
