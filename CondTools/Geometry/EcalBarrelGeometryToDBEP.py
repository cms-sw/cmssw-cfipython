import FWCore.ParameterSet.Config as cms

def EcalBarrelGeometryToDBEP(**kwargs):
  mod = cms.ESProducer('EcalBarrelGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
