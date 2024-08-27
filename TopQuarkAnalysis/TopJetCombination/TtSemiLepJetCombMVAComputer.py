import FWCore.ParameterSet.Config as cms

def TtSemiLepJetCombMVAComputer(**kwargs):
  mod = cms.EDProducer('TtSemiLepJetCombMVAComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
