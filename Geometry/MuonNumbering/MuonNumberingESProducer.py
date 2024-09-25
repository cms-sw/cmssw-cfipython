import FWCore.ParameterSet.Config as cms

def MuonNumberingESProducer(*args, **kwargs):
  mod = cms.ESProducer('MuonNumberingESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
