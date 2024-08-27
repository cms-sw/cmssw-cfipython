import FWCore.ParameterSet.Config as cms

def HcalSiPMCharacteristicsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalSiPMCharacteristicsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
