import FWCore.ParameterSet.Config as cms

hltLevel1Activity = cms.EDFilter('HLTLevel1Activity',
  L1GtReadoutRecordTag = cms.InputTag('hltGtDigis'),
  bunchCrossings = cms.vint32(
    0,
    -1,
    1
  ),
  daqPartitions = cms.uint32(1),
  ignoreL1Mask = cms.bool(False),
  invert = cms.bool(False),
  physicsLoBits = cms.uint64(1),
  physicsHiBits = cms.uint64(262144),
  technicalBits = cms.uint64(1)
)
