import FWCore.ParameterSet.Config as cms

triggerResultsFilter = cms.EDFilter('TriggerResultsFilter',
  hltResults = cms.InputTag('TriggerResults'),
  l1tResults = cms.InputTag('hltGtStage2Digis'),
  l1tIgnoreMaskAndPrescale = cms.bool(False),
  throw = cms.bool(True),
  triggerConditions = cms.vstring('HLT_*')
)
