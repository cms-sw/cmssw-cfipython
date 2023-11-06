import FWCore.ParameterSet.Config as cms

PFTauSecondaryVertexProducer = cms.EDProducer('PFTauSecondaryVertexProducer',
  PFTauTag = cms.InputTag('hpsPFTauProducer'),
  mightGet = cms.optional.untracked.vstring
)
