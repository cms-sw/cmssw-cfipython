import FWCore.ParameterSet.Config as cms

def EcalPedHists(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalPedHists',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
