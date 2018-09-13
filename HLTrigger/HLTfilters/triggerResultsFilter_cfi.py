import FWCore.ParameterSet.Config as cms

triggerResultsFilter = cms.EDFilter('TriggerResultsFilter',
  hltResults = cms.InputTag('TriggerResults'),
  l1tResults = cms.InputTag('hltGtDigis'),
  l1tIgnoreMask = cms.bool(False),
  l1techIgnorePrescales = cms.bool(False),
  daqPartitions = cms.uint32(1),
  throw = cms.bool(True),
  triggerConditions = cms.vstring('HLT_*')
)
