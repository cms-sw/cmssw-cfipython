import FWCore.ParameterSet.Config as cms

gctRawToDigi = cms.EDProducer('GctRawToDigi',
  unpackSharedRegions = cms.bool(False),
  numberOfGctSamplesToUnpack = cms.uint32(1),
  numberOfRctSamplesToUnpack = cms.uint32(1),
  hltMode = cms.bool(False),
  inputLabel = cms.InputTag('rawDataCollector'),
  unpackerVersion = cms.uint32(0),
  gctFedId = cms.untracked.int32(745),
  checkHeaders = cms.untracked.bool(False),
  verbose = cms.untracked.bool(False)
)
