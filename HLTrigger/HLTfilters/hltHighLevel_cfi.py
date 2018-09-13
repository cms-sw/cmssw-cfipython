import FWCore.ParameterSet.Config as cms

hltHighLevel = cms.EDFilter('HLTHighLevel',
  TriggerResultsTag = cms.InputTag('TriggerResults', '', 'HLT'),
  HLTPaths = cms.vstring(),
  eventSetupPathsKey = cms.string(''),
  andOr = cms.bool(True),
  throw = cms.bool(True)
)
