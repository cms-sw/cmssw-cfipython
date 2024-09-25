import FWCore.ParameterSet.Config as cms

def SiStripClusterizerConditionsGPUESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiStripClusterizerConditionsGPUESProducer',
    QualityLabel = cms.string(''),
    Label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
