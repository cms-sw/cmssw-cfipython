import FWCore.ParameterSet.Config as cms

def QGLikelihoodDBWriter(**kwargs):
  mod = cms.EDAnalyzer('QGLikelihoodDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
