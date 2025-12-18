import FWCore.ParameterSet.Config as cms

def MuonNumberingInitialization(*args, **kwargs):
  mod = cms.ESProducer('MuonNumberingInitialization',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
