import FWCore.ParameterSet.Config as cms

def HLTMuonRefMethod(*args, **kwargs):
  mod = cms.EDProducer('HLTMuonRefMethod',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
