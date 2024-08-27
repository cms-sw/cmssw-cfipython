import FWCore.ParameterSet.Config as cms

def HeavyIonCSVESProducer(**kwargs):
  mod = cms.ESProducer('HeavyIonCSVESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
