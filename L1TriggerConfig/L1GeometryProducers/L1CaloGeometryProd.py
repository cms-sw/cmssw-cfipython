import FWCore.ParameterSet.Config as cms

def L1CaloGeometryProd(*args, **kwargs):
  mod = cms.ESProducer('L1CaloGeometryProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
