import FWCore.ParameterSet.Config as cms

DTGeometryESModule = cms.ESProducer('DTGeometryESModule',
  fromDDD = cms.bool(True),
  fromDD4hep = cms.bool(False),
  DDDetector = cms.ESInputTag('', ''),
  alignmentsLabel = cms.string(''),
  appendToDataLabel = cms.string(''),
  attribute = cms.string('MuStructure'),
  value = cms.string('MuonBarrelDT'),
  applyAlignment = cms.bool(True)
)
