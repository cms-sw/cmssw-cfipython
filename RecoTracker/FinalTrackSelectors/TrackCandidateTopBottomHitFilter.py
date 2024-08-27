import FWCore.ParameterSet.Config as cms

def TrackCandidateTopBottomHitFilter(**kwargs):
  mod = cms.EDProducer('TrackCandidateTopBottomHitFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
