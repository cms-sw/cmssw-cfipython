import FWCore.ParameterSet.Config as cms

def SiStripRecHitMatcherESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiStripRecHitMatcherESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
