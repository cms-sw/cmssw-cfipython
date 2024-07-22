import FWCore.ParameterSet.Config as cms

def L1RCTChannelMaskOnlineProd(**kwargs):
  mod = cms.ESProducer('L1RCTChannelMaskOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod