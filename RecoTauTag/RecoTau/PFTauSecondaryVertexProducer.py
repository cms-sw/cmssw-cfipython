import FWCore.ParameterSet.Config as cms

def PFTauSecondaryVertexProducer(*args, **kwargs):
  mod = cms.EDProducer('PFTauSecondaryVertexProducer',
    PFTauTag = cms.InputTag('hpsPFTauProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
