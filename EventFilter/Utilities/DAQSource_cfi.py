import FWCore.ParameterSet.Config as cms

source = cms.Source('DAQSource',
  dataMode = cms.untracked.string('FRD'),
  eventChunkSize = cms.untracked.uint32(64),
  maxChunkSize = cms.untracked.uint32(0),
  eventChunkBlock = cms.untracked.uint32(0),
  numBuffers = cms.untracked.uint32(2),
  maxBufferedFiles = cms.untracked.uint32(2),
  alwaysStartFromfirstLS = cms.untracked.uint32(0),
  verifyChecksum = cms.untracked.bool(True),
  useL1EventID = cms.untracked.bool(False),
  testTCDSFEDRange = cms.untracked.vuint32(),
  fileListMode = cms.untracked.bool(False),
  fileNames = cms.untracked.vstring()
)
