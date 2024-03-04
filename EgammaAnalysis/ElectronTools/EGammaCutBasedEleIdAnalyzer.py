import FWCore.ParameterSet.Config as cms

def EGammaCutBasedEleIdAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EGammaCutBasedEleIdAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
