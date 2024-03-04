import FWCore.ParameterSet.Config as cms

def HydjetAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HydjetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
