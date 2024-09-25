import FWCore.ParameterSet.Config as cms

def DTGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('DTGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
