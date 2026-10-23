import FWCore.ParameterSet.Config as cms

def DTSegmentAnalysisTest(*args, **kwargs):
  mod = cms.EDProducer('DTSegmentAnalysisTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
