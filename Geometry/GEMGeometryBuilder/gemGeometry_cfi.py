import FWCore.ParameterSet.Config as cms

gemGeometry = cms.ESProducer('GEMGeometryESModule',
  fromDDD = cms.bool(True),
  fromDD4hep = cms.bool(False),
  applyAlignment = cms.bool(False),
  alignmentsLabel = cms.string(''),
  appendToDataLabel = cms.string('')
)
