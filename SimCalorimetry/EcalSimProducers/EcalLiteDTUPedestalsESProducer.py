import FWCore.ParameterSet.Config as cms

def EcalLiteDTUPedestalsESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalLiteDTUPedestalsESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
