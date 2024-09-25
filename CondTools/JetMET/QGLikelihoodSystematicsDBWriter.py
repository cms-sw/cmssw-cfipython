import FWCore.ParameterSet.Config as cms

def QGLikelihoodSystematicsDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('QGLikelihoodSystematicsDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
