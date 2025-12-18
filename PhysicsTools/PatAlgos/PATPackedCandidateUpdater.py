import FWCore.ParameterSet.Config as cms

def PATPackedCandidateUpdater(*args, **kwargs):
  mod = cms.EDProducer('PATPackedCandidateUpdater',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
