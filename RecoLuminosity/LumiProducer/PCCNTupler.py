import FWCore.ParameterSet.Config as cms

def PCCNTupler(**kwargs):
  mod = cms.EDAnalyzer('PCCNTupler',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
