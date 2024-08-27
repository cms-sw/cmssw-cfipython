import FWCore.ParameterSet.Config as cms

def TtFullLepJetPartonMatch(**kwargs):
  mod = cms.EDProducer('TtFullLepJetPartonMatch',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
