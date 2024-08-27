import FWCore.ParameterSet.Config as cms

def trgMatchIsolatedPixelTrackCandidateProducer(**kwargs):
  mod = cms.EDProducer('trgMatchIsolatedPixelTrackCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
