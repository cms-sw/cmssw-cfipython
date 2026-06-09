import FWCore.ParameterSet.Config as cms

def HLTriggerJSONMonitoring(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTriggerJSONMonitoring',
    triggerResults = cms.InputTag('TriggerResults', '', '@currentProcess'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
