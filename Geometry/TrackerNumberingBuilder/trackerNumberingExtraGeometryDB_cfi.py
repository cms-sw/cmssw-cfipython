import FWCore.ParameterSet.Config as cms

trackerNumberingExtraGeometryDB = cms.ESProducer('TrackerGeometricDetExtraESModule',
  fromDDD = cms.bool(False),
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
