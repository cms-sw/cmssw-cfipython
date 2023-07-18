import FWCore.ParameterSet.Config as cms

mtdNumberingGeometry = cms.ESProducer('MTDGeometricTimingDetESModule',
  fromDDD = cms.bool(True),
  fromDD4hep = cms.bool(False),
  appendToDataLabel = cms.string('')
)
