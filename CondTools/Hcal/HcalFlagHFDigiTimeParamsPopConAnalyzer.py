import FWCore.ParameterSet.Config as cms

def HcalFlagHFDigiTimeParamsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalFlagHFDigiTimeParamsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
