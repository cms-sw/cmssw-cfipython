import FWCore.ParameterSet.Config as cms

def HcalLongRecoParamsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalLongRecoParamsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
