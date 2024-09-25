import FWCore.ParameterSet.Config as cms

def hph_ProducerHPH(*args, **kwargs):
  mod = cms.ESProducer('hph::ProducerHPH',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
