import FWCore.ParameterSet.Config as cms

def PFTauSelector(**kwargs):
  mod = cms.EDFilter('PFTauSelector',
    src = cms.InputTag('fixedConePFTauProducer'),
    cut = cms.string('pt > 0'),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag('fixedConePFTauDiscriminationByIsolation'),
        selectionCut = cms.double(0.5)
      )
    ),
    discriminatorContainers = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
