import FWCore.ParameterSet.Config as cms

def EcalRechitChannelStatusGPUESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalRechitChannelStatusGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
