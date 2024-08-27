import FWCore.ParameterSet.Config as cms

def ParametrizedMagneticFieldProducer(**kwargs):
  mod = cms.ESProducer('ParametrizedMagneticFieldProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
