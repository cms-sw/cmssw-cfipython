import FWCore.ParameterSet.Config as cms

def HcalGainWidthsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalGainWidthsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
