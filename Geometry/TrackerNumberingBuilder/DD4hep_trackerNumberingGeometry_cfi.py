import FWCore.ParameterSet.Config as cms

DD4hep_trackerNumberingGeometry = cms.ESProducer('TrackerGeometricDetESModule',
  fromDDD = cms.bool(False),
  fromDD4hep = cms.bool(True),
  appendToDataLabel = cms.string('')
)
