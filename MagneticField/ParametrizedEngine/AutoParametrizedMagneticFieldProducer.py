import FWCore.ParameterSet.Config as cms

def AutoParametrizedMagneticFieldProducer(**kwargs):
  mod = cms.ESProducer('AutoParametrizedMagneticFieldProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
