import FWCore.ParameterSet.Config as cms

def SyncDCSO2O(**kwargs):
  mod = cms.EDAnalyzer('SyncDCSO2O',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
