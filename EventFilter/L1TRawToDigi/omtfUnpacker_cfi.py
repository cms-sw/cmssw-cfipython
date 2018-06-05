import FWCore.ParameterSet.Config as cms

omtfUnpacker = cms.EDProducer('OmtfUnpacker',
  inputLabel = cms.InputTag('rawDataCollector'),
  skipRpc = cms.bool(False),
  skipCsc = cms.bool(False),
  skipDt = cms.bool(False),
  skipMuon = cms.bool(False),
  useRpcConnectionFile = cms.bool(False),
  rpcConnectionFile = cms.string(''),
  outputTag = cms.string('')
)
