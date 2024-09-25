import FWCore.ParameterSet.Config as cms

def TestTriggerNames(*args, **kwargs):
  mod = cms.EDAnalyzer('TestTriggerNames',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
