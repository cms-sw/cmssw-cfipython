import FWCore.ParameterSet.Config as cms

def EcalHexDisplay(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalHexDisplay',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
