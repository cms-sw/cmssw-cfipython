import FWCore.ParameterSet.Config as cms

def TtSemiLepJetPartonMatch(**kwargs):
  mod = cms.EDProducer('TtSemiLepJetPartonMatch',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
