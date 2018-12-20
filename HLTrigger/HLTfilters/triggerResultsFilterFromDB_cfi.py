import FWCore.ParameterSet.Config as cms

triggerResultsFilterFromDB = cms.EDFilter('TriggerResultsFilterFromDB',
  hltResults = cms.InputTag('TriggerResults'),
  l1tResults = cms.InputTag('hltGtStage2Digis'),
  l1tIgnoreMaskAndPrescale = cms.bool(False),
  throw = cms.bool(True),
  eventSetupPathsKey = cms.string('')
)
