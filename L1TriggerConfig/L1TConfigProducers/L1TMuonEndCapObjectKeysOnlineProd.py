import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapObjectKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TMuonEndCapObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
