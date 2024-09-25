import FWCore.ParameterSet.Config as cms

def HcalConvertedPedestalsGPUESProducer(*args, **kwargs):
  mod = cms.ESProducer('HcalConvertedPedestalsGPUESProducer',
    ComponentName = cms.string(''),
    label0 = cms.string(''),
    label1 = cms.string(''),
    label2 = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
