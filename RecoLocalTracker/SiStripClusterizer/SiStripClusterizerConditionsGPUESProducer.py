import FWCore.ParameterSet.Config as cms

def SiStripClusterizerConditionsGPUESProducer(**kwargs):
  mod = cms.ESProducer('SiStripClusterizerConditionsGPUESProducer',
    QualityLabel = cms.string(''),
    Label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
