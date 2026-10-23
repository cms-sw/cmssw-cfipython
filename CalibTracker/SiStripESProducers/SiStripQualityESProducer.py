import FWCore.ParameterSet.Config as cms

def SiStripQualityESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiStripQualityESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
