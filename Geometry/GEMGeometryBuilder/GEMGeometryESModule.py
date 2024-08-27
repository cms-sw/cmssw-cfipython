import FWCore.ParameterSet.Config as cms

def GEMGeometryESModule(**kwargs):
  mod = cms.ESProducer('GEMGeometryESModule',
    fromDDD = cms.bool(True),
    fromDD4hep = cms.bool(False),
    applyAlignment = cms.bool(False),
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
