import FWCore.ParameterSet.Config as cms

RPCGeometryESModule = cms.ESProducer('RPCGeometryESModule',
  fromDDD = cms.untracked.bool(True),
  fromDD4hep = cms.untracked.bool(False),
  appendToDataLabel = cms.string('')
)
