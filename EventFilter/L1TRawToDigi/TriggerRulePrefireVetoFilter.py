import FWCore.ParameterSet.Config as cms

def TriggerRulePrefireVetoFilter(**kwargs):
  mod = cms.EDFilter('TriggerRulePrefireVetoFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
