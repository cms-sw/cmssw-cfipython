import FWCore.ParameterSet.Config as cms

def ElectronIsolatorFromEffectiveArea(**kwargs):
  mod = cms.EDFilter('ElectronIsolatorFromEffectiveArea',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
