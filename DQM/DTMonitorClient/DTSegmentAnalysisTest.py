import FWCore.ParameterSet.Config as cms

def DTSegmentAnalysisTest(**kwargs):
  mod = cms.EDProducer('DTSegmentAnalysisTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
