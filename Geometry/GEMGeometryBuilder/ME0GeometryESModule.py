import FWCore.ParameterSet.Config as cms

def ME0GeometryESModule(**kwargs):
  mod = cms.ESProducer('ME0GeometryESModule',
    fromDDD = cms.bool(True),
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
