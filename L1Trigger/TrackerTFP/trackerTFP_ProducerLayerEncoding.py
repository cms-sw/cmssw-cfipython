import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerLayerEncoding(**kwargs):
  mod = cms.ESProducer('trackerTFP::ProducerLayerEncoding',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
