import FWCore.ParameterSet.Config as cms

def UniformMagneticFieldESProducer(*args, **kwargs):
  mod = cms.ESProducer('UniformMagneticFieldESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
