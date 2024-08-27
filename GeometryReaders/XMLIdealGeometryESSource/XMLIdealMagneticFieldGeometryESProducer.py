import FWCore.ParameterSet.Config as cms

def XMLIdealMagneticFieldGeometryESProducer(**kwargs):
  mod = cms.ESProducer('XMLIdealMagneticFieldGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
