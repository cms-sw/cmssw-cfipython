import FWCore.ParameterSet.Config as cms

def QGLikelihoodDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('QGLikelihoodDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
