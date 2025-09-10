import FWCore.ParameterSet.Config as cms

def SiStripDelayESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiStripDelayESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
