import FWCore.ParameterSet.Config as cms

hltTrigReport = cms.EDAnalyzer('HLTrigReport',
  HLTriggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  reportBy = cms.untracked.string('job'),
  resetBy = cms.untracked.string('never'),
  serviceBy = cms.untracked.string('never'),
  CustomDatasets = cms.untracked.PSet(),
  CustomStreams = cms.untracked.PSet(),
  ReferencePath = cms.untracked.string('HLTriggerFinalPath'),
  ReferenceRate = cms.untracked.double(100)
)
