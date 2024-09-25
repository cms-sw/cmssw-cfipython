import FWCore.ParameterSet.Config as cms

def TriggerSummaryAnalyzerRAW(*args, **kwargs):
  mod = cms.EDAnalyzer('TriggerSummaryAnalyzerRAW',
    inputTag = cms.InputTag('hltTriggerSummaryRAW'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
