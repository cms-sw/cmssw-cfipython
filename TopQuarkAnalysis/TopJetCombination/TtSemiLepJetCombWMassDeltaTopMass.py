import FWCore.ParameterSet.Config as cms

def TtSemiLepJetCombWMassDeltaTopMass(**kwargs):
  mod = cms.EDProducer('TtSemiLepJetCombWMassDeltaTopMass',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
