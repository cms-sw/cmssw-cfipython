import FWCore.ParameterSet.Config as cms

def L1TriggerJSONMonitoring(**kwargs):
  mod = cms.EDAnalyzer('L1TriggerJSONMonitoring',
    L1Results = cms.InputTag('hltGtStage2Digis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
