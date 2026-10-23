import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapForestESProducer(*args, **kwargs):
  mod = cms.ESProducer('L1TMuonEndCapForestESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
