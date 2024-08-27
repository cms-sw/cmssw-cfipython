import FWCore.ParameterSet.Config as cms

def EcalLaserAPDPNRatiosRefGPUESProducer(**kwargs):
  mod = cms.ESProducer('EcalLaserAPDPNRatiosRefGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
