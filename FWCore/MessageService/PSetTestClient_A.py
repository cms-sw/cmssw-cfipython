import FWCore.ParameterSet.Config as cms

def PSetTestClient_A(**kwargs):
  mod = cms.EDAnalyzer('PSetTestClient_A',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
