import FWCore.ParameterSet.Config as cms

def HcalRecoParamsWithPulseShapesGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalRecoParamsWithPulseShapesGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
