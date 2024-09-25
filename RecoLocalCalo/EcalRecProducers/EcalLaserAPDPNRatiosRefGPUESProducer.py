import FWCore.ParameterSet.Config as cms

def EcalLaserAPDPNRatiosRefGPUESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalLaserAPDPNRatiosRefGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
