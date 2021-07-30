import FWCore.ParameterSet.Config as cms

muonGeometryConstants = cms.ESProducer('MuonGeometryConstantsESModule',
  fromDD4Hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
