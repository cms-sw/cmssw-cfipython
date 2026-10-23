import FWCore.ParameterSet.Config as cms

def MkFitGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('MkFitGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
