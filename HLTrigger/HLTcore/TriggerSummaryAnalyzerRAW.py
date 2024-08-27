import FWCore.ParameterSet.Config as cms

def TriggerSummaryAnalyzerRAW(**kwargs):
  mod = cms.EDAnalyzer('TriggerSummaryAnalyzerRAW',
    inputTag = cms.InputTag('hltTriggerSummaryRAW'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
