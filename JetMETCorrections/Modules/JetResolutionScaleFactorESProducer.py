import FWCore.ParameterSet.Config as cms

def JetResolutionScaleFactorESProducer(**kwargs):
  mod = cms.ESProducer('JetResolutionScaleFactorESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
