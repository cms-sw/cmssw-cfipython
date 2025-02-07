import FWCore.ParameterSet.Config as cms

def SimAnalyzerMinbias(*args, **kwargs):
  mod = cms.EDAnalyzer('SimAnalyzerMinbias',
    TimeCut = cms.untracked.double(500),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
