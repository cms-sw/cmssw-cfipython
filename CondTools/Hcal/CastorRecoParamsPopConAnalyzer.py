import FWCore.ParameterSet.Config as cms

def CastorRecoParamsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorRecoParamsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
