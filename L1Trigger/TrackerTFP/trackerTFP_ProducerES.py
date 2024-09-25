import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerES(*args, **kwargs):
  mod = cms.ESProducer('trackerTFP::ProducerES',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
