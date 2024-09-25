import FWCore.ParameterSet.Config as cms

def EcalPedOffset(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalPedOffset',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
