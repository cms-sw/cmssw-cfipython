import FWCore.ParameterSet.Config as cms

def HLTMuonValidator(*args, **kwargs):
  mod = cms.EDProducer('HLTMuonValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
