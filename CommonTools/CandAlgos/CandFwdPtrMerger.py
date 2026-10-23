import FWCore.ParameterSet.Config as cms

def CandFwdPtrMerger(*args, **kwargs):
  mod = cms.EDProducer('CandFwdPtrMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
