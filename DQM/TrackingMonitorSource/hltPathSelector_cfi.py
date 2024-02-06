import FWCore.ParameterSet.Config as cms

hltPathSelector = cms.EDFilter('HLTPathSelector',
  verbose = cms.untracked.bool(False),
  processName = cms.string(''),
  hltPathsOfInterest = cms.vstring(),
  triggerResults = cms.untracked.InputTag('TriggerResults', '', 'HLT'),
  triggerEvent = cms.untracked.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  mightGet = cms.optional.untracked.vstring
)
