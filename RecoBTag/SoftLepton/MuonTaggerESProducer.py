import FWCore.ParameterSet.Config as cms

def MuonTaggerESProducer(*args, **kwargs):
  mod = cms.ESProducer('MuonTaggerESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
