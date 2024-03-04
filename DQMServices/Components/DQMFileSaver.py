import FWCore.ParameterSet.Config as cms

def DQMFileSaver(**kwargs):
  mod = cms.EDAnalyzer('DQMFileSaver',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
