import FWCore.ParameterSet.Config as cms

def MagneticFieldMapESProducer(*args, **kwargs):
  mod = cms.ESProducer('MagneticFieldMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
