import FWCore.ParameterSet.Config as cms

def PixelNtupletsFitterProducer(*args, **kwargs):
  mod = cms.EDProducer('PixelNtupletsFitterProducer',
    useRiemannFit = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
