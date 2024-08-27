import FWCore.ParameterSet.Config as cms

def StoreEcalCondition(**kwargs):
  mod = cms.EDAnalyzer('StoreEcalCondition',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
