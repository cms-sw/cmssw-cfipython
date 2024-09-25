import FWCore.ParameterSet.Config as cms

def SyncDCSO2O(*args, **kwargs):
  mod = cms.EDAnalyzer('SyncDCSO2O',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
