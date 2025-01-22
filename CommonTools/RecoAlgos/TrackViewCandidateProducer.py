import FWCore.ParameterSet.Config as cms

def TrackViewCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackViewCandidateProducer',
    src = cms.InputTag(''),
    particleType = cms.string('pi+'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
