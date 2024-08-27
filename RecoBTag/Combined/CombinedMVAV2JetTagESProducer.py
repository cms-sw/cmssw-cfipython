import FWCore.ParameterSet.Config as cms

def CombinedMVAV2JetTagESProducer(**kwargs):
  mod = cms.ESProducer('CombinedMVAV2JetTagESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
