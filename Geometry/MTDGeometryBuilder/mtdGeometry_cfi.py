import FWCore.ParameterSet.Config as cms

mtdGeometry = cms.ESProducer('MTDDigiGeometryESModule',
  appendToDataLabel = cms.string(''),
  fromDDD = cms.bool(True),
  applyAlignment = cms.bool(True),
  alignmentsLabel = cms.string('')
)
