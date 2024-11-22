import FWCore.ParameterSet.Config as cms

def CombinedMVAV2JetTagESProducer(*args, **kwargs):
  mod = cms.ESProducer('CombinedMVAV2JetTagESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
