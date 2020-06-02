import FWCore.ParameterSet.Config as cms

me0Geometry = cms.ESProducer('ME0GeometryESModule',
  useDDD = cms.bool(True),
  useDD4Hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
