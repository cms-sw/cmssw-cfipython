import FWCore.ParameterSet.Config as cms

def HcalDbProducer(*args, **kwargs):
  mod = cms.ESProducer('HcalDbProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
