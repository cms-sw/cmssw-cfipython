import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerDataFormats(*args, **kwargs):
  mod = cms.ESProducer('trackerTFP::ProducerDataFormats',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
