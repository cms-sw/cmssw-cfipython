import FWCore.ParameterSet.Config as cms

def DTResolutionAnalysisTask(*args, **kwargs):
  mod = cms.EDProducer('DTResolutionAnalysisTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
