import FWCore.ParameterSet.Config as cms

def CastorGeometryFromDBEP(**kwargs):
  mod = cms.ESProducer('CastorGeometryFromDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
