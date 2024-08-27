import FWCore.ParameterSet.Config as cms

def PFTauSecondaryVertexProducer(**kwargs):
  mod = cms.EDProducer('PFTauSecondaryVertexProducer',
    PFTauTag = cms.InputTag('hpsPFTauProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
