import FWCore.ParameterSet.Config as cms

def SiStripRecHitMatcherESProducer(**kwargs):
  mod = cms.ESProducer('SiStripRecHitMatcherESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
