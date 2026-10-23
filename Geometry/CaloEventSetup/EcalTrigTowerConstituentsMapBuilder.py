import FWCore.ParameterSet.Config as cms

def EcalTrigTowerConstituentsMapBuilder(*args, **kwargs):
  mod = cms.ESProducer('EcalTrigTowerConstituentsMapBuilder',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
