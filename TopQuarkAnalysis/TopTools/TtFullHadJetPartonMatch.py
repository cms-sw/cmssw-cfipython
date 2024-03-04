import FWCore.ParameterSet.Config as cms

def TtFullHadJetPartonMatch(**kwargs):
  mod = cms.EDProducer('TtFullHadJetPartonMatch',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
