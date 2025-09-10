import FWCore.ParameterSet.Config as cms

def L1MuGMTScalesProducer(*args, **kwargs):
  mod = cms.ESProducer('L1MuGMTScalesProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
