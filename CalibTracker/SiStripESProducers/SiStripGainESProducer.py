import FWCore.ParameterSet.Config as cms

def SiStripGainESProducer(**kwargs):
  mod = cms.ESProducer('SiStripGainESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
