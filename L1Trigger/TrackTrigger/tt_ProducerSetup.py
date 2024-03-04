import FWCore.ParameterSet.Config as cms

def tt_ProducerSetup(**kwargs):
  mod = cms.ESProducer('tt::ProducerSetup',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
