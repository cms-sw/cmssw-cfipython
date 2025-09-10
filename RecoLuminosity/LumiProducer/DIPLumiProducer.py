import FWCore.ParameterSet.Config as cms

def DIPLumiProducer(*args, **kwargs):
  mod = cms.ESSource('DIPLumiProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
