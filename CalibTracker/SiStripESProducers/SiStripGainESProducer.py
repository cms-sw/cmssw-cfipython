import FWCore.ParameterSet.Config as cms

def SiStripGainESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiStripGainESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
