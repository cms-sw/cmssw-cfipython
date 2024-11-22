import FWCore.ParameterSet.Config as cms

def L2MuonCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('L2MuonCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
