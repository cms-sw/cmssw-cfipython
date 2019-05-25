import FWCore.ParameterSet.Config as cms

mtdGeometryDB = cms.ESProducer('MTDDigiGeometryESModule',
  appendToDataLabel = cms.string(''),
  fromDDD = cms.bool(False),
  applyAlignment = cms.bool(True),
  alignmentsLabel = cms.string('')
)
