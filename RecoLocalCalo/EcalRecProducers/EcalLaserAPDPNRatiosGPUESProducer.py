import FWCore.ParameterSet.Config as cms

def EcalLaserAPDPNRatiosGPUESProducer(**kwargs):
  mod = cms.ESProducer('EcalLaserAPDPNRatiosGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
