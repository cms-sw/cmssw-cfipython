import FWCore.ParameterSet.Config as cms

def PFClusterRefCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('PFClusterRefCandidateProducer',
    src = cms.InputTag(''),
    particleType = cms.string('pi+'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
