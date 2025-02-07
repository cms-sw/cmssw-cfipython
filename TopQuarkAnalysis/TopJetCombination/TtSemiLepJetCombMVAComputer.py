import FWCore.ParameterSet.Config as cms

def TtSemiLepJetCombMVAComputer(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepJetCombMVAComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
