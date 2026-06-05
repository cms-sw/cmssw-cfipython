import FWCore.ParameterSet.Config as cms

def TtSemiLepJetPartonMatch(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepJetPartonMatch',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
