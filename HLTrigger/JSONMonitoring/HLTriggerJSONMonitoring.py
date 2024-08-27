import FWCore.ParameterSet.Config as cms

def HLTriggerJSONMonitoring(**kwargs):
  mod = cms.EDAnalyzer('HLTriggerJSONMonitoring',
    triggerResults = cms.InputTag('TriggerResults', '', '@currentProcess'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
