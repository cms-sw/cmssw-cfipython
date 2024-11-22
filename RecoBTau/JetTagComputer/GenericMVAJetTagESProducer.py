import FWCore.ParameterSet.Config as cms

def GenericMVAJetTagESProducer(*args, **kwargs):
  mod = cms.ESProducer('GenericMVAJetTagESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
