import FWCore.ParameterSet.Config as cms

def HcalConvertedEffectivePedestalWidthsGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalConvertedEffectivePedestalWidthsGPUESProducer',
    ComponentName = cms.string(''),
    label0 = cms.string(''),
    label1 = cms.string(''),
    label2 = cms.string(''),
    label3 = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
