import FWCore.ParameterSet.Config as cms

def L1TMuonGlobalParamsOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TMuonGlobalParamsOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
