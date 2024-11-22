import FWCore.ParameterSet.Config as cms

def TestHistoryKeeping(*args, **kwargs):
  mod = cms.EDAnalyzer('TestHistoryKeeping',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
