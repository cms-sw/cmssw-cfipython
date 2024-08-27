import FWCore.ParameterSet.Config as cms

def UniformMagneticFieldESProducer(**kwargs):
  mod = cms.ESProducer('UniformMagneticFieldESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
