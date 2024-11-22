import FWCore.ParameterSet.Config as cms

def DQMStoreStats(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMStoreStats',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
