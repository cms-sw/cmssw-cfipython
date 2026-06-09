import FWCore.ParameterSet.Config as cms

def PFTauSelector(*args, **kwargs):
  mod = cms.EDFilter('PFTauSelector',
    src = cms.InputTag('fixedConePFTauProducer'),
    cut = cms.string('pt > 0'),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag('fixedConePFTauDiscriminationByIsolation'),
        selectionCut = cms.double(0.5)
      ),
      template = cms.PSetTemplate(
        discriminator = cms.required.InputTag,
        selectionCut = cms.required.double
      )
    ),
    discriminatorContainers = cms.VPSet(
      template = cms.PSetTemplate(
        discriminator = cms.required.InputTag,
        rawValues = cms.required.vstring,
        workingPoints = cms.required.vstring,
        selectionCuts = cms.required.vdouble
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
