import FWCore.ParameterSet.Config as cms

def L1TTwinMuxParamsESProducer(*args, **kwargs):
  mod = cms.ESProducer('L1TTwinMuxParamsESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
