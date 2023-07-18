import FWCore.ParameterSet.Config as cms

trackerNumberingGeometryDB = cms.ESProducer('TrackerGeometricDetESModule',
  fromDDD = cms.bool(False),
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
