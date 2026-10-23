import FWCore.ParameterSet.Config as cms

def EGammaCutBasedEleIdAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EGammaCutBasedEleIdAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
