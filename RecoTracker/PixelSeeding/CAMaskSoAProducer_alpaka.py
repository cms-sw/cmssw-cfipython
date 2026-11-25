import FWCore.ParameterSet.Config as cms

def CAMaskSoAProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('CAMaskSoAProducer@alpaka',
    oldMask = cms.InputTag(''),
    hitSoAs = cms.VInputTag(),
    trackSoA = cms.InputTag('pixelTracksHighPtAlpaka'),
    minQuality = cms.string('highPurity'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
