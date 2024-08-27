import FWCore.ParameterSet.Config as cms

def VolumeBasedMagneticFieldESProducer(**kwargs):
  mod = cms.ESProducer('VolumeBasedMagneticFieldESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
