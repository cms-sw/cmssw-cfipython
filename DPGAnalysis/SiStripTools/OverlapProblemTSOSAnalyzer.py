import FWCore.ParameterSet.Config as cms

def OverlapProblemTSOSAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('OverlapProblemTSOSAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
