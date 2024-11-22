import FWCore.ParameterSet.Config as cms

def XMLIdealMagneticFieldGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('XMLIdealMagneticFieldGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
