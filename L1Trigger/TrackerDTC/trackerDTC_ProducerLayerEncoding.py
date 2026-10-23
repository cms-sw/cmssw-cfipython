import FWCore.ParameterSet.Config as cms

def trackerDTC_ProducerLayerEncoding(*args, **kwargs):
  mod = cms.ESProducer('trackerDTC::ProducerLayerEncoding',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
