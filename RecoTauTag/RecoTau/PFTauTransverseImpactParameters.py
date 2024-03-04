import FWCore.ParameterSet.Config as cms

def PFTauTransverseImpactParameters(**kwargs):
  mod = cms.EDProducer('PFTauTransverseImpactParameters',
    PFTauPVATag = cms.InputTag('PFTauPrimaryVertexProducer'),
    useFullCalculation = cms.bool(False),
    PFTauTag = cms.InputTag('hpsPFTauProducer'),
    PFTauSVATag = cms.InputTag('PFTauSecondaryVertexProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
