import FWCore.ParameterSet.Config as cms

def HcalTrigTowerGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('HcalTrigTowerGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
