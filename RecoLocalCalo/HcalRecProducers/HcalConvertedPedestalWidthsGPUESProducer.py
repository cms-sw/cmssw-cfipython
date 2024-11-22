import FWCore.ParameterSet.Config as cms

def HcalConvertedPedestalWidthsGPUESProducer(*args, **kwargs):
  mod = cms.ESProducer('HcalConvertedPedestalWidthsGPUESProducer',
    ComponentName = cms.string(''),
    label0 = cms.string(''),
    label1 = cms.string(''),
    label2 = cms.string(''),
    label3 = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
