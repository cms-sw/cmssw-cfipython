import FWCore.ParameterSet.Config as cms

trackerNumberingGeometry = cms.ESProducer('TrackerGeometricDetESModule',
  fromDDD = cms.bool(True),
  appendToDataLabel = cms.string('')
)
