import FWCore.ParameterSet.Config as cms

def L1MuGMTChannelMaskOnlineProducer(**kwargs):
  mod = cms.ESProducer('L1MuGMTChannelMaskOnlineProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
