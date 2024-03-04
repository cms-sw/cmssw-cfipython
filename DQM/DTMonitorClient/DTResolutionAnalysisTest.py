import FWCore.ParameterSet.Config as cms

def DTResolutionAnalysisTest(**kwargs):
  mod = cms.EDProducer('DTResolutionAnalysisTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
