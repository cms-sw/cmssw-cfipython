import FWCore.ParameterSet.Config as cms

def L1MuTriggerScalesOnlineProducer(**kwargs):
  mod = cms.ESProducer('L1MuTriggerScalesOnlineProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
