import FWCore.ParameterSet.Config as cms

def HcalPulseDelaysPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalPulseDelaysPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
