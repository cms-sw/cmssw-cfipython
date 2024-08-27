import FWCore.ParameterSet.Config as cms

def DoodadESProducer(**kwargs):
  mod = cms.ESProducer('DoodadESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
