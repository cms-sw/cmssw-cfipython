import FWCore.ParameterSet.Config as cms

def EcalPulseCovariancesGPUESProducer(**kwargs):
  mod = cms.ESProducer('EcalPulseCovariancesGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
