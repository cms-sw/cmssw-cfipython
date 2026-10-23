import FWCore.ParameterSet.Config as cms

def TriggerRulePrefireVetoFilter(*args, **kwargs):
  mod = cms.EDFilter('TriggerRulePrefireVetoFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
