import FWCore.ParameterSet.Config as cms

trackerGeometry = cms.ESProducer('TrackerDigiGeometryESModule',
  appendToDataLabel = cms.string(''),
  fromDDD = cms.bool(True),
  applyAlignment = cms.bool(True),
  alignmentsLabel = cms.string('')
)
