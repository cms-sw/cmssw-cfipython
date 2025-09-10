import FWCore.ParameterSet.Config as cms

def PackedCandidatePtrMerger(*args, **kwargs):
  mod = cms.EDProducer('PackedCandidatePtrMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
