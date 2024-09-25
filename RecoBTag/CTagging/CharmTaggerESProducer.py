import FWCore.ParameterSet.Config as cms

def CharmTaggerESProducer(*args, **kwargs):
  mod = cms.ESProducer('CharmTaggerESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
