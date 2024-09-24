import FWCore.ParameterSet.Config as cms

def GenJetFlavourInfoPreserver(*args, **kwargs):
  mod = cms.EDProducer('GenJetFlavourInfoPreserver',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod