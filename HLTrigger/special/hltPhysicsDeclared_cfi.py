import FWCore.ParameterSet.Config as cms

hltPhysicsDeclared = cms.EDFilter('HLTPhysicsDeclared',
  L1GtReadoutRecordTag = cms.InputTag('hltGtDigis'),
  invert = cms.bool(False)
)
