import FWCore.ParameterSet.Config as cms

def EcalLaserCorrectionServiceMC(*args, **kwargs):
  mod = cms.ESProducer('EcalLaserCorrectionServiceMC',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
