import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapForestOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TMuonEndCapForestOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
