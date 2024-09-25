import FWCore.ParameterSet.Config as cms

def ElectronIsolatorFromEffectiveArea(*args, **kwargs):
  mod = cms.EDFilter('ElectronIsolatorFromEffectiveArea',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
