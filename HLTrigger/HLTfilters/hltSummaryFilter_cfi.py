import FWCore.ParameterSet.Config as cms

hltSummaryFilter = cms.EDFilter('HLTSummaryFilter',
  saveTags = cms.bool(True),
  summary = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  member = cms.InputTag('hlt1jet30', '', 'HLT'),
  cut = cms.string('pt>80'),
  minN = cms.int32(1)
)
