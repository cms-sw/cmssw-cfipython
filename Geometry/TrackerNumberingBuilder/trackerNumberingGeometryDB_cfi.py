import FWCore.ParameterSet.Config as cms

trackerNumberingGeometryDB = cms.ESProducer('TrackerGeometricDetESModule',
  fromDDD = cms.bool(False),
  appendToDataLabel = cms.string('')
)
