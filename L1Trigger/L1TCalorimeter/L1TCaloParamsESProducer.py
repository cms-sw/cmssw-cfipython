import FWCore.ParameterSet.Config as cms

def L1TCaloParamsESProducer(**kwargs):
  mod = cms.ESProducer('L1TCaloParamsESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
