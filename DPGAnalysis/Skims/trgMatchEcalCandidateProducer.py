import FWCore.ParameterSet.Config as cms

def trgMatchEcalCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchEcalCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
