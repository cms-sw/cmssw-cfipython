import FWCore.ParameterSet.Config as cms

def StoreEcalCondition(*args, **kwargs):
  mod = cms.EDAnalyzer('StoreEcalCondition',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
