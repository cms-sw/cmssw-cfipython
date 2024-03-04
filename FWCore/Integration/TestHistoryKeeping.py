import FWCore.ParameterSet.Config as cms

def TestHistoryKeeping(**kwargs):
  mod = cms.EDAnalyzer('TestHistoryKeeping',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
