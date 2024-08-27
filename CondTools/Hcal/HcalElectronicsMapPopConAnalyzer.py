import FWCore.ParameterSet.Config as cms

def HcalElectronicsMapPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalElectronicsMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
