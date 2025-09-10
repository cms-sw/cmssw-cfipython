import FWCore.ParameterSet.Config as cms

trackerNumberingGeometry = cms.ESProducer('TrackerGeometricDetESModule',
  fromDDD = cms.bool(True),
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
