import FWCore.ParameterSet.Config as cms

def trackerTFP_ProducerFormatsKF(**kwargs):
  mod = cms.ESProducer('trackerTFP::ProducerFormatsKF',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
