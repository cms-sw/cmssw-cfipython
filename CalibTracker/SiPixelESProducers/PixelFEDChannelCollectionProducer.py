import FWCore.ParameterSet.Config as cms

def PixelFEDChannelCollectionProducer(*args, **kwargs):
  mod = cms.ESProducer('PixelFEDChannelCollectionProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
