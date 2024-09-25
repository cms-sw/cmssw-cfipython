import FWCore.ParameterSet.Config as cms

def FFTPFJetSysCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPFJetSysCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
