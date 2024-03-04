import FWCore.ParameterSet.Config as cms

def RKTest(**kwargs):
  mod = cms.EDAnalyzer('RKTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
