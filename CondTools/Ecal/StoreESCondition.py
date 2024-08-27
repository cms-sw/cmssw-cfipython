import FWCore.ParameterSet.Config as cms

def StoreESCondition(**kwargs):
  mod = cms.EDAnalyzer('StoreESCondition',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
