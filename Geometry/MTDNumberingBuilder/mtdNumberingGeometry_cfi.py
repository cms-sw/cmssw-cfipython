import FWCore.ParameterSet.Config as cms

mtdNumberingGeometry = cms.ESProducer('MTDGeometricTimingDetESModule',
  fromDDD = cms.bool(True),
  appendToDataLabel = cms.string('')
)
