import FWCore.ParameterSet.Config as cms

def ZElectronsSelectorAndSkim(*args, **kwargs):
  mod = cms.EDFilter('ZElectronsSelectorAndSkim',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
