import FWCore.ParameterSet.Config as cms

def TtSemiLepHypWMassDeltaTopMass(**kwargs):
  mod = cms.EDProducer('TtSemiLepHypWMassDeltaTopMass',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
