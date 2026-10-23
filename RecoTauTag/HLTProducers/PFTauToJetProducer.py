import FWCore.ParameterSet.Config as cms

def PFTauToJetProducer(*args, **kwargs):
  mod = cms.EDProducer('PFTauToJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
