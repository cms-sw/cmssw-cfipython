import FWCore.ParameterSet.Config as cms

def SiStripGainSimESProducer(**kwargs):
  mod = cms.ESProducer('SiStripGainSimESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
