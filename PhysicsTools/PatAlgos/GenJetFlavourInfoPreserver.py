import FWCore.ParameterSet.Config as cms

def GenJetFlavourInfoPreserver(**kwargs):
  mod = cms.EDProducer('GenJetFlavourInfoPreserver',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
