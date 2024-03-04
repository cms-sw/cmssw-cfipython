import FWCore.ParameterSet.Config as cms

def EcalLiteDTUPedestalsESProducer(**kwargs):
  mod = cms.ESProducer('EcalLiteDTUPedestalsESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
