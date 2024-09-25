import FWCore.ParameterSet.Config as cms

def MuonTaggerNoIPESProducer(*args, **kwargs):
  mod = cms.ESProducer('MuonTaggerNoIPESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
