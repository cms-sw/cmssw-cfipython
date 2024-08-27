import FWCore.ParameterSet.Config as cms

def CastorGeometryToDBEP(**kwargs):
  mod = cms.ESProducer('CastorGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
