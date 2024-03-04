import FWCore.ParameterSet.Config as cms

def SimAnalyzerMinbias(**kwargs):
  mod = cms.EDAnalyzer('SimAnalyzerMinbias',
    TimeCut = cms.untracked.double(500),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
