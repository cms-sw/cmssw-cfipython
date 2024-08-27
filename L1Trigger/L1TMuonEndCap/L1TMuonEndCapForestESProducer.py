import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapForestESProducer(**kwargs):
  mod = cms.ESProducer('L1TMuonEndCapForestESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
