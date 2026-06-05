import FWCore.ParameterSet.Config as cms

def RPCConeBuilder(*args, **kwargs):
  mod = cms.ESProducer('RPCConeBuilder',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
