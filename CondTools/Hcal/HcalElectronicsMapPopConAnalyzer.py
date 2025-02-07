import FWCore.ParameterSet.Config as cms

def HcalElectronicsMapPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalElectronicsMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
