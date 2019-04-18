import FWCore.ParameterSet.Config as cms

source = cms.Source('FedRawDataInputSource',
  eventChunkSize = cms.untracked.uint32(32),
  eventChunkBlock = cms.untracked.uint32(32),
  numBuffers = cms.untracked.uint32(2),
  maxBufferedFiles = cms.untracked.uint32(2),
  verifyAdler32 = cms.untracked.bool(True),
  verifyChecksum = cms.untracked.bool(True),
  useL1EventID = cms.untracked.bool(False),
  fileListMode = cms.untracked.bool(False),
  fileNames = cms.untracked.vstring()
)
