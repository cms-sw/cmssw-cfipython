import FWCore.ParameterSet.Config as cms

me0Geometry = cms.ESProducer('ME0GeometryESModule',
  fromDDD = cms.bool(True),
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
