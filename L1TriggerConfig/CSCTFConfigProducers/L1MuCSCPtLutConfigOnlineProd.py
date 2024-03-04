import FWCore.ParameterSet.Config as cms

def L1MuCSCPtLutConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1MuCSCPtLutConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
