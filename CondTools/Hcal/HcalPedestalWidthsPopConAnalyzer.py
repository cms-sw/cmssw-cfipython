import FWCore.ParameterSet.Config as cms

def HcalPedestalWidthsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalPedestalWidthsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
