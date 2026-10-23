import FWCore.ParameterSet.Config as cms

def DTGeometryESModule(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
