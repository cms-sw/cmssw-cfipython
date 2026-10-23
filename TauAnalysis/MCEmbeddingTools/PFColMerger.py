import FWCore.ParameterSet.Config as cms

def PFColMerger(*args, **kwargs):
  mod = cms.EDProducer('PFColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
