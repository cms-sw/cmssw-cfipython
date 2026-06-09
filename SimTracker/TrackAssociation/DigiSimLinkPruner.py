import FWCore.ParameterSet.Config as cms

def DigiSimLinkPruner(*args, **kwargs):
  mod = cms.EDProducer('DigiSimLinkPruner',
    trackingParticles = cms.required.InputTag,
    pixelSimLinkSrc = cms.InputTag('simSiPixelDigis'),
    stripSimLinkSrc = cms.optional.InputTag,
    phase2OTSimLinkSrc = cms.optional.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
