import FWCore.ParameterSet.Config as cms

def L3MuonCleaner(**kwargs):
  mod = cms.EDProducer('L3MuonCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
