import FWCore.ParameterSet.Config as cms

def HcalTrigTowerGeometryESProducer(**kwargs):
  mod = cms.ESProducer('HcalTrigTowerGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
