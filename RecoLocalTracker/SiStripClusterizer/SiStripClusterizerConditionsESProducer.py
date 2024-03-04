import FWCore.ParameterSet.Config as cms

def SiStripClusterizerConditionsESProducer(**kwargs):
  mod = cms.ESProducer('SiStripClusterizerConditionsESProducer',
    QualityLabel = cms.string(''),
    Label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
