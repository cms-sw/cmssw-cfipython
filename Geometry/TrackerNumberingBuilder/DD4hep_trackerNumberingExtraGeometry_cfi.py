import FWCore.ParameterSet.Config as cms

DD4hep_trackerNumberingExtraGeometry = cms.ESProducer('TrackerGeometricDetExtraESModule',
  fromDDD = cms.bool(False),
  fromDD4hep = cms.bool(True),
  appendToDataLabel = cms.string('')
)
