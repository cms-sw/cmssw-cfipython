import FWCore.ParameterSet.Config as cms

def EcalDccWeightBuilder(**kwargs):
  mod = cms.EDAnalyzer('EcalDccWeightBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
