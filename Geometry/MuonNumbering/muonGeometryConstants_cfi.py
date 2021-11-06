import FWCore.ParameterSet.Config as cms

muonGeometryConstants = cms.ESProducer('MuonGeometryConstantsESModule',
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
