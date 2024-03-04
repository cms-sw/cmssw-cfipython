import FWCore.ParameterSet.Config as cms

def EcalTimeBiasCorrectionsFillInitial(**kwargs):
  mod = cms.EDAnalyzer('EcalTimeBiasCorrectionsFillInitial',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
