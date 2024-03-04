import FWCore.ParameterSet.Config as cms

def PixelNtupletsFitterProducer(**kwargs):
  mod = cms.EDProducer('PixelNtupletsFitterProducer',
    useRiemannFit = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
