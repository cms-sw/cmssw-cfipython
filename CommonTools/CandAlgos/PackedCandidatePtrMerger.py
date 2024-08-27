import FWCore.ParameterSet.Config as cms

def PackedCandidatePtrMerger(**kwargs):
  mod = cms.EDProducer('PackedCandidatePtrMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
