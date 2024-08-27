import FWCore.ParameterSet.Config as cms

def EcalBarrelGeometryEPdd4hep(**kwargs):
  mod = cms.ESProducer('EcalBarrelGeometryEPdd4hep',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
