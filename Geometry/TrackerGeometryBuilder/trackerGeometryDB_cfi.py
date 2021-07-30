import FWCore.ParameterSet.Config as cms

trackerGeometryDB = cms.ESProducer('TrackerDigiGeometryESModule',
  appendToDataLabel = cms.string(''),
  fromDDD = cms.bool(False),
  applyAlignment = cms.bool(True),
  alignmentsLabel = cms.string('')
)
