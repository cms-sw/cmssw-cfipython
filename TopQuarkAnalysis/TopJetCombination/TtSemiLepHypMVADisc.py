import FWCore.ParameterSet.Config as cms

def TtSemiLepHypMVADisc(**kwargs):
  mod = cms.EDProducer('TtSemiLepHypMVADisc',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
