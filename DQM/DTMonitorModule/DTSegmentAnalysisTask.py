import FWCore.ParameterSet.Config as cms

def DTSegmentAnalysisTask(**kwargs):
  mod = cms.EDProducer('DTSegmentAnalysisTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
