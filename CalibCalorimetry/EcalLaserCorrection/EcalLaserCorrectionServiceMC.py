import FWCore.ParameterSet.Config as cms

def EcalLaserCorrectionServiceMC(**kwargs):
  mod = cms.ESProducer('EcalLaserCorrectionServiceMC',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
