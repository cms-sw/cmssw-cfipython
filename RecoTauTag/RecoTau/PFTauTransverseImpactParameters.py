import FWCore.ParameterSet.Config as cms

def PFTauTransverseImpactParameters(*args, **kwargs):
  mod = cms.EDProducer('PFTauTransverseImpactParameters',
    PFTauPVATag = cms.InputTag('PFTauPrimaryVertexProducer'),
    useFullCalculation = cms.bool(False),
    PFTauTag = cms.InputTag('hpsPFTauProducer'),
    PFTauSVATag = cms.InputTag('PFTauSecondaryVertexProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
