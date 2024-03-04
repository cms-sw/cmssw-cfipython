import FWCore.ParameterSet.Config as cms

def ESDaqInfoTask(**kwargs):
  mod = cms.EDAnalyzer('ESDaqInfoTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
