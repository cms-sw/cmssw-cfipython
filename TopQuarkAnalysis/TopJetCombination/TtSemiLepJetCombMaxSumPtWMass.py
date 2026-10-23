import FWCore.ParameterSet.Config as cms

def TtSemiLepJetCombMaxSumPtWMass(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepJetCombMaxSumPtWMass',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
