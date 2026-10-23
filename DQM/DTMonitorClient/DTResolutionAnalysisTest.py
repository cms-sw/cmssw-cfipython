import FWCore.ParameterSet.Config as cms

def DTResolutionAnalysisTest(*args, **kwargs):
  mod = cms.EDProducer('DTResolutionAnalysisTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
