import FWCore.ParameterSet.Config as cms

def DTGeometryESModule(**kwargs):
  mod = cms.ESProducer('DTGeometryESModule',
    fromDDD = cms.bool(True),
    fromDD4hep = cms.bool(False),
    DDDetector = cms.ESInputTag('', ''),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    attribute = cms.string('MuStructure'),
    value = cms.string('MuonBarrelDT'),
    applyAlignment = cms.bool(True)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
