import FWCore.ParameterSet.Config as cms

trackerNumberingSLHCGeometryDB = cms.ESProducer('TrackerGeometricDetESModule',
  fromDDD = cms.bool(False),
  layerNumberPXB = cms.uint32(18),
  totalBlade = cms.uint32(56),
  appendToDataLabel = cms.string('')
)
