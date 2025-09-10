import FWCore.ParameterSet.Config as cms

mtdNumberingGeometryDB = cms.ESProducer('MTDGeometricTimingDetESModule',
  fromDDD = cms.bool(False),
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
