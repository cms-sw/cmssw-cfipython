import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerES(**kwargs):
  mod = cms.ESProducer('trackerTFP::ProducerES',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
