import FWCore.ParameterSet.Config as cms

def HcalPFCutsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalPFCutsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
