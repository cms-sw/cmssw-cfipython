import FWCore.ParameterSet.Config as cms

def ParametrizedMagneticFieldProducer(*args, **kwargs):
  mod = cms.ESProducer('ParametrizedMagneticFieldProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
