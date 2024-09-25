import FWCore.ParameterSet.Config as cms

def VolumeBasedMagneticFieldESProducer(*args, **kwargs):
  mod = cms.ESProducer('VolumeBasedMagneticFieldESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
