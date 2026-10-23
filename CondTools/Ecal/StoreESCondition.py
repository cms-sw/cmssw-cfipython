import FWCore.ParameterSet.Config as cms

def StoreESCondition(*args, **kwargs):
  mod = cms.EDAnalyzer('StoreESCondition',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
