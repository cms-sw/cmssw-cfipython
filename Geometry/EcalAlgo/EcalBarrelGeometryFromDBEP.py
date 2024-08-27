import FWCore.ParameterSet.Config as cms

def EcalBarrelGeometryFromDBEP(**kwargs):
  mod = cms.ESProducer('EcalBarrelGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
