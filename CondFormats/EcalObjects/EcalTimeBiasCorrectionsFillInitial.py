import FWCore.ParameterSet.Config as cms

def EcalTimeBiasCorrectionsFillInitial(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalTimeBiasCorrectionsFillInitial',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
