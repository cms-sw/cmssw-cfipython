import FWCore.ParameterSet.Config as cms

def CastorDbProducer(*args, **kwargs):
  mod = cms.ESProducer('CastorDbProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
