import FWCore.ParameterSet.Config as cms

def PatTriggerTagAndProbe(*args, **kwargs):
  mod = cms.EDAnalyzer('PatTriggerTagAndProbe',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
