import FWCore.ParameterSet.Config as cms

def EcalLinearCorrectionsGPUESProducer(**kwargs):
  mod = cms.ESProducer('EcalLinearCorrectionsGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
