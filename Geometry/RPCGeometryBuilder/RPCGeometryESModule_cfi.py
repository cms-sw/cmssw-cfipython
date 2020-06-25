import FWCore.ParameterSet.Config as cms

RPCGeometryESModule = cms.ESProducer('RPCGeometryESModule',
  useDDD = cms.untracked.bool(True),
  useDD4hep = cms.untracked.bool(False),
  appendToDataLabel = cms.string('')
)
