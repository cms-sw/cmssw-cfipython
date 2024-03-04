import FWCore.ParameterSet.Config as cms

def L1TMuonBarrelParamsOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TMuonBarrelParamsOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
