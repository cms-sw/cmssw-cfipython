import FWCore.ParameterSet.Config as cms

mtdNumberingGeometryDB = cms.ESProducer('MTDGeometricTimingDetESModule',
  fromDDD = cms.bool(False),
  appendToDataLabel = cms.string('')
)
