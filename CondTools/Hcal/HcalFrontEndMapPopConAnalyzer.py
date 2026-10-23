import FWCore.ParameterSet.Config as cms

def HcalFrontEndMapPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalFrontEndMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
