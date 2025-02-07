import FWCore.ParameterSet.Config as cms

def SegmentTrackAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('SegmentTrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
