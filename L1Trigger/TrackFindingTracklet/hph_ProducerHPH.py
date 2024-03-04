import FWCore.ParameterSet.Config as cms

def hph_ProducerHPH(**kwargs):
  mod = cms.ESProducer('hph::ProducerHPH',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
