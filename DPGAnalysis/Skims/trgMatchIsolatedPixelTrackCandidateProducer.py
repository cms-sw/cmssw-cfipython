import FWCore.ParameterSet.Config as cms

def trgMatchIsolatedPixelTrackCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchIsolatedPixelTrackCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
