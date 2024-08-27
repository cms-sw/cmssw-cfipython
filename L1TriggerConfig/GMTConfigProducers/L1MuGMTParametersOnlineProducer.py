import FWCore.ParameterSet.Config as cms

def L1MuGMTParametersOnlineProducer(**kwargs):
  mod = cms.ESProducer('L1MuGMTParametersOnlineProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
