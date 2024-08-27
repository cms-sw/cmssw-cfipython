import FWCore.ParameterSet.Config as cms

def MagneticFieldMapESProducer(**kwargs):
  mod = cms.ESProducer('MagneticFieldMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
