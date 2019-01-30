import FWCore.ParameterSet.Config as cms

trackerNumberingSLHCGeometry = cms.ESProducer('TrackerGeometricDetESModule',
  fromDDD = cms.bool(True),
  layerNumberPXB = cms.uint32(18),
  totalBlade = cms.uint32(56),
  appendToDataLabel = cms.string('')
)
