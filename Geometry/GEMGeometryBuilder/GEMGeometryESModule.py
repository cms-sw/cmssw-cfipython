import FWCore.ParameterSet.Config as cms

def GEMGeometryESModule(*args, **kwargs):
  mod = cms.ESProducer('GEMGeometryESModule',
    fromDDD = cms.bool(True),
    fromDD4hep = cms.bool(False),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
