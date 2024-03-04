import FWCore.ParameterSet.Config as cms

def HGCalGeometryToDBEP(**kwargs):
  mod = cms.ESProducer('HGCalGeometryToDBEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
