import FWCore.ParameterSet.Config as cms

def FFTPFJetCorrectionESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPFJetCorrectionESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
