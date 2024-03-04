import FWCore.ParameterSet.Config as cms

def TtSemiLepHypMaxSumPtWMass(**kwargs):
  mod = cms.EDProducer('TtSemiLepHypMaxSumPtWMass',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
