import FWCore.ParameterSet.Config as cms

def L1TCaloStage2ParamsESProducer(**kwargs):
  mod = cms.ESProducer('L1TCaloStage2ParamsESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
