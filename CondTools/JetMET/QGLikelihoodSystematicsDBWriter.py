import FWCore.ParameterSet.Config as cms

def QGLikelihoodSystematicsDBWriter(**kwargs):
  mod = cms.EDAnalyzer('QGLikelihoodSystematicsDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
