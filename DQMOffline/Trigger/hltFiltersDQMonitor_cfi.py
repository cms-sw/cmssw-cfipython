import FWCore.ParameterSet.Config as cms

hltFiltersDQMonitor = cms.EDProducer('HLTFiltersDQMonitor',
  folderName = cms.string('HLT/Filters'),
  efficPlotNamePrefix = cms.string('effic_'),
  triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
  triggerSummaryAOD = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  triggerSummaryRAW = cms.InputTag('hltTriggerSummaryRAW', '', 'HLT'),
  mightGet = cms.optional.untracked.vstring
)
