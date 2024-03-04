import FWCore.ParameterSet.Config as cms

def L1TMuonBarrelObjectKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TMuonBarrelObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
