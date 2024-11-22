import FWCore.ParameterSet.Config as cms

def PatTriggerAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatTriggerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
