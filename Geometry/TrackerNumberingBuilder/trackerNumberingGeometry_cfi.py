import FWCore.ParameterSet.Config as cms

trackerNumberingGeometry = cms.ESProducer('TrackerGeometricDetESModule',
  fromDDD = cms.bool(True),
  layerNumberPXB = cms.uint32(16),
  totalBlade = cms.uint32(24),
  appendToDataLabel = cms.string('')
)
