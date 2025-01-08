import FWCore.ParameterSet.Config as cms

def ChargedCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('ChargedCandidateProducer',
    src = cms.InputTag(''),
    particleType = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
