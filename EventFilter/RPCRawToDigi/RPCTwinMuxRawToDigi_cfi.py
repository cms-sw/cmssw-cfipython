import FWCore.ParameterSet.Config as cms

RPCTwinMuxRawToDigi = cms.EDProducer('RPCTwinMuxRawToDigi',
  inputTag = cms.InputTag('rawDataCollector'),
  calculateCRC = cms.bool(True),
  fillCounters = cms.bool(True),
  bxMin = cms.int32(-2),
  bxMax = cms.int32(2)
)
