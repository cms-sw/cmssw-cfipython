import FWCore.ParameterSet.Config as cms

def L1MuGMTScalesProducer(**kwargs):
  mod = cms.ESProducer('L1MuGMTScalesProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
