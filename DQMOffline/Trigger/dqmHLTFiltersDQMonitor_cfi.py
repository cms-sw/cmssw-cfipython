import FWCore.ParameterSet.Config as cms

dqmHLTFiltersDQMonitor = cms.EDProducer('HLTFiltersDQMonitor',
  folderName = cms.string('HLT/Filters'),
  efficPlotNamePrefix = cms.string('effic_'),
  triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  triggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  triggerEventWithRefs = cms.InputTag('hltTriggerSummaryRAW', '', 'HLT'),
  mightGet = cms.optional.untracked.vstring
)
