import FWCore.ParameterSet.Config as cms

def SegmentTrackAnalyzer(**kwargs):
  mod = cms.EDProducer('SegmentTrackAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
