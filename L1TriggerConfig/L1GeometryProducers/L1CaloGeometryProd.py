import FWCore.ParameterSet.Config as cms

def L1CaloGeometryProd(**kwargs):
  mod = cms.ESProducer('L1CaloGeometryProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
