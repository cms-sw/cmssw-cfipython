import FWCore.ParameterSet.Config as cms

def CSCSegmentColCleaner(*args, **kwargs):
  mod = cms.EDProducer('CSCSegmentColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
