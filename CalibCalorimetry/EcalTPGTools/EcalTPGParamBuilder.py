import FWCore.ParameterSet.Config as cms

def EcalTPGParamBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTPGParamBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
