import FWCore.ParameterSet.Config as cms

def HcalRecoParamsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalRecoParamsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
