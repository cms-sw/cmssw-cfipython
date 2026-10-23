import FWCore.ParameterSet.Config as cms

def HtrXmlPattern(*args, **kwargs):
  mod = cms.EDAnalyzer('HtrXmlPattern',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
