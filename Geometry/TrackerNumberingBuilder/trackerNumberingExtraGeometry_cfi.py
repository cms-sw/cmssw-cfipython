import FWCore.ParameterSet.Config as cms

trackerNumberingExtraGeometry = cms.ESProducer('TrackerGeometricDetExtraESModule',
  fromDDD = cms.bool(True),
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
