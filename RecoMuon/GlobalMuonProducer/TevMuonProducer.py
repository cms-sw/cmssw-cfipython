import FWCore.ParameterSet.Config as cms

def TevMuonProducer(*args, **kwargs):
  mod = cms.EDProducer('TevMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
