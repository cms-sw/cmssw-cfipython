import FWCore.ParameterSet.Config as cms

def EcalDccWeightBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalDccWeightBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
