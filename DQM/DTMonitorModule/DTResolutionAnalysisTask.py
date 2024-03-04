import FWCore.ParameterSet.Config as cms

def DTResolutionAnalysisTask(**kwargs):
  mod = cms.EDProducer('DTResolutionAnalysisTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
