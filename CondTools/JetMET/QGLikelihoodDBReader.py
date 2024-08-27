import FWCore.ParameterSet.Config as cms

def QGLikelihoodDBReader(**kwargs):
  mod = cms.EDAnalyzer('QGLikelihoodDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
