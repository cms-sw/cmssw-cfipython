import FWCore.ParameterSet.Config as cms

def EcalTimeBiasCorrectionsGPUESProducer(**kwargs):
  mod = cms.ESProducer('EcalTimeBiasCorrectionsGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
