import FWCore.ParameterSet.Config as cms

def EcalTPGParamBuilder(**kwargs):
  mod = cms.EDAnalyzer('EcalTPGParamBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod