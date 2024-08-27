import FWCore.ParameterSet.Config as cms

def L1MuTriggerScalesProducer(**kwargs):
  mod = cms.ESProducer('L1MuTriggerScalesProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
