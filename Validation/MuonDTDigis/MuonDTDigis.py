import FWCore.ParameterSet.Config as cms

def MuonDTDigis(*args, **kwargs):
  mod = cms.EDProducer('MuonDTDigis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
