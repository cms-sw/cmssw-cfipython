import FWCore.ParameterSet.Config as cms

triggerSummaryAnalyzerRAW = cms.EDAnalyzer('TriggerSummaryAnalyzerRAW',
  inputTag = cms.InputTag('hltTriggerSummaryRAW'),
  mightGet = cms.optional.untracked.vstring
)
