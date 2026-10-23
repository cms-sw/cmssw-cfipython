import FWCore.ParameterSet.Config as cms

def PFConcretePFCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('PFConcretePFCandidateProducer',
    src = cms.InputTag('particleFlow'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
