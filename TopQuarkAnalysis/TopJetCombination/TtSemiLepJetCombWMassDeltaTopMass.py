import FWCore.ParameterSet.Config as cms

def TtSemiLepJetCombWMassDeltaTopMass(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepJetCombWMassDeltaTopMass',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
