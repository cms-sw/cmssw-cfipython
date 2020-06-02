import FWCore.ParameterSet.Config as cms

gemGeometry = cms.ESProducer('GEMGeometryESModule',
  useDDD = cms.bool(True),
  useDD4Hep = cms.bool(False),
  applyAlignment = cms.bool(False),
  alignmentsLabel = cms.string(''),
  appendToDataLabel = cms.string('')
)
