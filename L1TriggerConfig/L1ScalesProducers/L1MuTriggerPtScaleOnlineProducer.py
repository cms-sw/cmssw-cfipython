import FWCore.ParameterSet.Config as cms

def L1MuTriggerPtScaleOnlineProducer(**kwargs):
  mod = cms.ESProducer('L1MuTriggerPtScaleOnlineProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
