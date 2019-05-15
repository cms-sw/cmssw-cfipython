import FWCore.ParameterSet.Config as cms

alcaIsolatedBunchSelector = cms.EDFilter('AlCaIsolatedBunchSelector',
  triggerResultLabel = cms.InputTag('TriggerResults', '', 'HLT'),
  processName = cms.string('HLT'),
  triggerName = cms.string('HLT_HcalIsolatedBunch')
)
