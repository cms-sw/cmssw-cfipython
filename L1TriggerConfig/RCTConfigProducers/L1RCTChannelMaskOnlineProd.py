import FWCore.ParameterSet.Config as cms

def L1RCTChannelMaskOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('L1RCTChannelMaskOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
