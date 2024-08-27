import FWCore.ParameterSet.Config as cms

def LHEWriter(**kwargs):
  mod = cms.EDAnalyzer('LHEWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
