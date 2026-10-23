import FWCore.ParameterSet.Config as cms

def JetResolutionScaleFactorESProducer(*args, **kwargs):
  mod = cms.ESProducer('JetResolutionScaleFactorESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
