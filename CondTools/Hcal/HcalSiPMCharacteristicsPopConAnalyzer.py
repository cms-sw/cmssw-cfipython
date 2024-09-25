import FWCore.ParameterSet.Config as cms

def HcalSiPMCharacteristicsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalSiPMCharacteristicsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
