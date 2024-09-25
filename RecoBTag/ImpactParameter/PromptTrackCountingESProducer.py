import FWCore.ParameterSet.Config as cms

def PromptTrackCountingESProducer(*args, **kwargs):
  mod = cms.ESProducer('PromptTrackCountingESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
