import FWCore.ParameterSet.Config as cms

def OverlapProblemTSOSAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('OverlapProblemTSOSAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
