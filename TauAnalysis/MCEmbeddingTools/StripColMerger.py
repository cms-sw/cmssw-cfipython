import FWCore.ParameterSet.Config as cms

def StripColMerger(*args, **kwargs):
  mod = cms.EDProducer('StripColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
