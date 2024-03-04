import FWCore.ParameterSet.Config as cms

def PixelFEDChannelCollectionProducer(**kwargs):
  mod = cms.ESProducer('PixelFEDChannelCollectionProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
