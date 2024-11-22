import FWCore.ParameterSet.Config as cms

def EcalDisplaysByEvent(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalDisplaysByEvent',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
