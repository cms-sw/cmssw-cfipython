import FWCore.ParameterSet.Config as cms

PFTauTransverseImpactParameters = cms.EDProducer('PFTauTransverseImpactParameters',
  PFTauPVATag = cms.InputTag('PFTauPrimaryVertexProducer'),
  useFullCalculation = cms.bool(False),
  PFTauTag = cms.InputTag('hpsPFTauProducer'),
  PFTauSVATag = cms.InputTag('PFTauSecondaryVertexProducer'),
  mightGet = cms.optional.untracked.vstring
)
