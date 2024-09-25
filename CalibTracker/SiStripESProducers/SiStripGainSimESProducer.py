import FWCore.ParameterSet.Config as cms

def SiStripGainSimESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiStripGainSimESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
