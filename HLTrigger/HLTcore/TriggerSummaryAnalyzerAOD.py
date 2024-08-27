import FWCore.ParameterSet.Config as cms

def TriggerSummaryAnalyzerAOD(**kwargs):
  mod = cms.EDAnalyzer('TriggerSummaryAnalyzerAOD',
    inputTag = cms.InputTag('hltTriggerSummaryAOD'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
