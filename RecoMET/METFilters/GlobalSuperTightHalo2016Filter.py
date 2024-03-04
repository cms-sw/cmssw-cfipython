import FWCore.ParameterSet.Config as cms

def GlobalSuperTightHalo2016Filter(**kwargs):
  mod = cms.EDFilter('GlobalSuperTightHalo2016Filter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
