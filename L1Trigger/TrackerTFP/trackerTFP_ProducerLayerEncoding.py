import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerLayerEncoding(*args, **kwargs):
  mod = cms.ESProducer('trackerTFP::ProducerLayerEncoding',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
