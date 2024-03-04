import FWCore.ParameterSet.Config as cms

def PromptTrackCountingESProducer(**kwargs):
  mod = cms.ESProducer('PromptTrackCountingESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
