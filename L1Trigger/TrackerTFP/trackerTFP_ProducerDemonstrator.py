import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerDemonstrator(**kwargs):
  mod = cms.ESProducer('trackerTFP::ProducerDemonstrator',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
