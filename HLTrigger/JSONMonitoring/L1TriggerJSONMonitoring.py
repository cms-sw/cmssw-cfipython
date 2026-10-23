import FWCore.ParameterSet.Config as cms

def L1TriggerJSONMonitoring(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TriggerJSONMonitoring',
    L1Results = cms.InputTag('hltGtStage2Digis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
