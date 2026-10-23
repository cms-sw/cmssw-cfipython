import FWCore.ParameterSet.Config as cms

def ME0GeometryESModule(*args, **kwargs):
  mod = cms.ESProducer('ME0GeometryESModule',
    fromDDD = cms.bool(True),
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
