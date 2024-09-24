import FWCore.ParameterSet.Config as cms

def DTNoiseAnalysisTest(*args, **kwargs):
  mod = cms.EDProducer('DTNoiseAnalysisTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
