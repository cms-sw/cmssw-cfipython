import FWCore.ParameterSet.Config as cms

def EcalBarrelGeometryEPdd4hep(*args, **kwargs):
  mod = cms.ESProducer('EcalBarrelGeometryEPdd4hep',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
