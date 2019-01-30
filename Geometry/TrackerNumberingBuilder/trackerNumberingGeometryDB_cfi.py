import FWCore.ParameterSet.Config as cms

trackerNumberingGeometryDB = cms.ESProducer('TrackerGeometricDetESModule',
  fromDDD = cms.bool(False),
  layerNumberPXB = cms.uint32(16),
  totalBlade = cms.uint32(24),
  appendToDataLabel = cms.string('')
)
