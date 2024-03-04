import FWCore.ParameterSet.Config as cms

def HGCalValidScintTest(**kwargs):
  mod = cms.EDAnalyzer('HGCalValidScintTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
