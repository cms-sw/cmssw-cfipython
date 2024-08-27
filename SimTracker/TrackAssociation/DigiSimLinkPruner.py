import FWCore.ParameterSet.Config as cms

def DigiSimLinkPruner(**kwargs):
  mod = cms.EDProducer('DigiSimLinkPruner',
    trackingParticles = cms.required.InputTag,
    pixelSimLinkSrc = cms.InputTag('simSiPixelDigis'),
    stripSimLinkSrc = cms.optional.InputTag,
    phase2OTSimLinkSrc = cms.optional.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
