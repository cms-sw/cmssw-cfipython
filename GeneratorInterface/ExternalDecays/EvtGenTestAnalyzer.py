import FWCore.ParameterSet.Config as cms

def EvtGenTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EvtGenTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
