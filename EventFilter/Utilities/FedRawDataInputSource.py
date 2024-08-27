import FWCore.ParameterSet.Config as cms

def FedRawDataInputSource(**kwargs):
  mod = cms.Source('FedRawDataInputSource',
    eventChunkSize = cms.untracked.uint32(32),
    eventChunkBlock = cms.untracked.uint32(32),
    numBuffers = cms.untracked.uint32(2),
    maxBufferedFiles = cms.untracked.uint32(2),
    alwaysStartFromfirstLS = cms.untracked.uint32(0),
    verifyChecksum = cms.untracked.bool(True),
    useL1EventID = cms.untracked.bool(False),
    testTCDSFEDRange = cms.untracked.vuint32(),
    fileListMode = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring()
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
